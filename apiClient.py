#!/usr/bin/env python
# coding=UTF-8
'''
	 # note：调用Http Json协议的接口。
	 # author：TavisD
	 # time：2016-9-4 16:58
	 # version: 1.0
	 #
'''

import hashlib
import json
from Crypto.Cipher import AES
from Crypto.Cipher import DES3
import base64
import requests
import re


class APIClient( ):
    def __init__( self ):
        self.AES_BASE_KEY = "Jq2VtktMAyqnMqenGH/FDQ=="  # 不能改
        self.APP_ID = "app110887164"  # 不能改
        self.APP_SECURITY = "454b42cf-3447-4782-8b62-38b933c2524d"  # 不能改
        self.DEFAULT_TOKEN = "JCeFOs2lw2myA1N31AlEeRKhBKMW4JexdWpilBuA"  # 不能改，万能token，用来获取登录token

    def cal_url( self, env, project_name, interface_name ):
        '''
        生成最终请求的url
        :param env: 环境，beta、fix、stg、release
        :param project_name:工程名称
        :param interface_name:接口名
        :return:
        '''
        env_url = { "beta": "test", "fix": "fix" }
        url = "http://" + env_url[ env ] + "." + project_name + "-api.hd/" + interface_name
        return url

    def cal_token( self, username, password, login_type = "NORMAL", env = "beta" ):
        '''
        生成token
        :param username:用户名
        :param password:密码
        :param login_type:业主端：NORMAL，供应商：SUPPLIER，运营后台：MANAGER。物业后台：PMMANAGER。默认生成业主端的token。
        :param env:环境。beta、Fix。
        :return:
        '''
        #
        if (login_type == "NORMAL"):
            params = { "loginName": username, "password": password }
            url = self.cal_url( env, "sso", "sso/login" )
            try:
                result = self.http_post( params, url, None )
                if result is not None:
                    return result[ "result" ]
            except Exception as e:
                print("生成NORMAL token出错！" + str( e ))
        elif (login_type == "SUPPLIER"):
            params = { "username": username, "password": password }
            url = self.cal_url( env, "supplier", "supplierSso/login" )
            try:
                result = self.http_post( params, url, None, login_type = login_type )
                if result is not None:
                    token_result = json.loads( result[ "result" ] )
                    return token_result[ "token" ]
            except Exception as e:
                print("生成SUPPLIER token出错！" + str( e ))
        elif (login_type == "MANAGER"):
            params = { "username": username, "password": password, "systemType": 2 }
            url = self.cal_url( env, "sys-sso", "systemSso/loginSys" )
            try:
                result = self.http_post( params, url, None )
                if result is not None:
                    return result[ "result" ]
            except Exception as e:
                print("生成MANAGER token出错！" + str( e ))
        elif (login_type == "PMMANAGER"):
            params = { "username": username, "password": password, "systemType": 1 }
            url = self.cal_url( env, "sys-sso", "systemSso/loginSys" )
            try:
                result = self.http_post( params, url, None )
                if result is not None:
                    return result[ "result" ]
            except Exception as e:
                print("生成PMMANAGER token出错！" + str( e ))

    def cal_signature( self, params ):
        '''
        生成MD5加密过的签名
        :param params:Dict格式
        :return:
        '''
        # 1.使用json解决传递的参数双引号会变成单引号问题。
        # 2.使用separators参数解决字典转json后有空白字符的问题。
        if (isinstance( params, dict )):
            params = json.dumps( params, separators = (',', ':') )
            content = str( params ) + self.APP_ID + self.APP_SECURITY
            # 加密
            m = hashlib.md5( )
            if (isinstance( content, str )):
                m.update( content.encode( 'utf-8' ) )
                return (m.hexdigest( )).upper( )
        else:
            print("生成签名失败！")

    def cal_secret( self, token, crypto_type ):
        '''
        生成密钥
        :param token:token凭证
        :param crypto_type:加密的类型
        :return:
        '''
        if (token == None or token == ""):
            token = self.DEFAULT_TOKEN
        # hash前先编码
        source_content = (token + self.AES_BASE_KEY).encode( "utf-8" )
        # SHA-256算法生成64位16进制字符串
        sha_result = hashlib.sha256( source_content ).hexdigest( )
        # 根据算法类型截取密钥
        if "AES" == crypto_type:
            key_length = 16
        elif "3DES" == crypto_type:
            key_length = 24
        else:
            return None
        secret = sha_result[ 0:key_length ]
        return secret

    def AES_encrypt( self, content, secret ):
        '''
        使用AES-128算法加密
        :param content:待加密内容
        :param secret: 密钥
        :return:
        '''
        BLOCK_SIZE = 16  # must be 16, 24, or 32 for AES。16（AES-128）、24（AES-192）、或32（AES-256）
        pad = lambda s: s + (BLOCK_SIZE - len( s ) % BLOCK_SIZE) * chr(
                BLOCK_SIZE - len( s ) % BLOCK_SIZE )  # 填充位数函数，填充成16位的倍数
        try:
            obj = AES.new( secret, AES.MODE_ECB )  # 使用密钥生成一个加密对象。
            crypt = obj.encrypt( pad( content ) )  # 加密
            return base64.b64encode( crypt ).decode( 'utf-8' )  # 最终生成base64编码的加密内容，并从byte类型decode回str
        except Exception as e:
            print("AES加密失败！" + str( e ))

    def AES_decrypt( self, content, secret ):
        '''
        使用AES-128算法解密
        :param content:待解密内容，base64编码
        :param secret:密钥
        :return:
        '''
        try:
            content = base64.b64decode( content )  # 先把base64编码内容转换成字节码
            obj = AES.new( secret, AES.MODE_ECB )  # 使用密钥生成一个加密对象。
            return obj.decrypt( content ).decode( 'utf-8' )  # 解密，并从byte类型decode回str
        except Exception as e:
            print("AES解密失败！" + str( e ))

    def DES3_encrypt( self, content, secret ):
        '''
        使用3DES算法加密
        :param content: 待加密内容
        :param secret: 密钥
        :return:
        '''

        BLOCK_SIZE = 8  # 3DES用8位填充
        pad = lambda s: s + (BLOCK_SIZE - len( s ) % BLOCK_SIZE) * chr(
                BLOCK_SIZE - len( s ) % BLOCK_SIZE )  # 填充函数

        try:
            encryptor = DES3.new( secret, DES3.MODE_ECB )  # 使用密钥生成一个加密对象
            crypt = encryptor.encrypt( pad( content ) )  # 加密
            return base64.b64encode( crypt ).decode( 'utf-8' )  # 最终生成base64编码的加密内容，并从byte类型decode回str
        except Exception as e:
            print("3DES加密失败！" + str( e ))

    def DES3_decrypt( self, content, secret ):
        '''
        使用3DES算法解密
        :param content: 待解密内容，base64编码
        :param secret: 密钥
        :return:
        '''
        try:
            content = base64.b64decode( content )  # 先把base64编码内容转换成字节码
            obj = DES3.new( secret, DES3.MODE_ECB )  # 使用密钥生成一个加密对象。
            return obj.decrypt( content ).decode( 'utf-8' )  # 解密，并从byte类型decode回str
        except Exception as e:
            print("3DES解密失败！" + str( e ))

    def http_post( self, params, url, token, login_type = "NORMAL", crypto_type = "3DES" ):
        '''
        http Post请求
        :param params: 请求参数，Dict类型
        :param url: 请求url
        :param login_type: 登录类型，NORMAL（APP）、SUPPLIER（商家）、MANAGE（管理员）
        :param token:登录的token
        :param crypto_type:加密方式，AES、3DES。默认为3DES。
        :return:返回解密后的response
        '''
        # 设置headers
        headers = { "content-type": "application/x-json", "x-client-appId": self.APP_ID }
        if (crypto_type == "3DES"):
            headers[ "x-client-fruit" ] = "mango"
        elif (crypto_type == "AES"):
            headers[ "x-client-fruit" ] = "watermelon"
        if (login_type == "NORMAL"):
            headers[ "x-client-type" ] = "app"
            headers[ "x-client-os" ] = "ios"
            headers[ "x-security-token" ] = token
        elif (login_type == "SUPPLIER"):
            headers[ "x-client-type" ] = "pc"
            headers[ "x-client-os" ] = "web"
            headers[ "x-supplier-token" ] = token
        elif (login_type == "MANAGER"):
            headers[ "x-client-type" ] = "pc"
            headers[ "x-client-os" ] = "platform"
            headers[ "x-manager-token" ] = token

        # 设置请求内容
        print("请求参数：===============>\n" + json.dumps( params, separators = (',', ':') ))
        signature = self.cal_signature( params )
        post_content = { "signature": signature, "params": params }
        if (isinstance( post_content, dict )):
            post_content = json.dumps( post_content, separators = (',', ':') )

            if (crypto_type == "AES"):
                # AES加密后的请求内容
                secret = self.cal_secret( token, "AES" )
                payload = self.AES_encrypt( post_content, secret )

                result = None
                # 发送HTTP Post请求
                try:
                    response = requests.post( url, data = payload, headers = headers )
                    # 解析HTTP响应
                    try:
                        if (response.status_code == 200):
                            json_temp = json.loads( response.text )
                            # print( 'AES解密前的结果：===============>\n' + str( json_temp ) )
                            if (json_temp[ "msgCode" ] == 200):
                                decrypt_result = self.AES_decrypt( str( json_temp[ "data" ] ), secret )
                                s = re.compile( '[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]' ).sub( '', decrypt_result )
                                result = json.loads( s )
                            else:
                                print('后端返回结果：===============>\n' + str( json_temp ))
                        else:
                            print('HTTP返回结果：===============>\n' + response.text)
                    except Exception as e:
                        print("解析AES响应失败!" + str( e ))
                except Exception as e:
                    print("http请求失败！" + str( e ))
                return result

            elif (crypto_type == "3DES"):
                # 3DES加密后的请求内容
                secret = self.cal_secret( token, "3DES" )
                payload = self.DES3_encrypt( post_content, secret )

                # 发送HTTP Post请求
                try:
                    response = requests.post( url, data = payload, headers = headers )
                    # 解析HTTP响应
                    result = None
                    try:
                        if (response.status_code == 200):
                            json_temp = json.loads( response.text )
                            # print( '3DES解密前的结果：===============>\n' + str( json_temp ) )
                            if (json_temp[ "msgCode" ] == 200):
                                decrypt_result = self.DES3_decrypt( str( json_temp[ "data" ] ), secret )
                                s = re.compile( '[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f]' ).sub( '',
                                                                                             decrypt_result )  # 过滤返回结果的转义字符
                                result = json.loads( s )
                            else:
                                print('后端返回结果：===============>\n' + str( json_temp ))
                        else:
                            print('HTTP返回结果：===============>\n' + response.text)
                    except Exception as e:
                        print("解析3DES响应失败!" + str( e ))
                    return result
                except Exception as e:
                    print("http请求失败！" + str( e ))
        else:
            print("请求参数必须是Dict类型！")

# #Demo 获取商家token
# api_client=APIClient()
# result=api_client.cal_token("username","password","SUPPLIER")#传入用户名、密码
# print(result)
#
# #Demo 获取业主token
# api_client=APIClient()
# result=api_client.cal_token("username","password")
# print(result)

# #Demo 获取运营后台token
# api_client=APIClient()
# result=api_client.cal_token("username","password","MANAGER","fix")
# print(result)

# # Demo 发送请求
# api_client = APIClient( )
# params = { "addressId": 121 }
# url = "http://test.user-api.hd/user/consignment/findByAddressId"
# token = "QgNvWUkSHyLjYXHhCu0w0X08b1rPxP7k7LlWRmLGDGA="
# result = api_client.http_post( params, url,  token ,"NORMAL",crypto_type = "3DES")
# print( result )

#
# # Demo 解析请求数据
# api_client = APIClient( )
# req_content = "od0X5J7qSnmbRd7eid24yuG9IygUX3lkSApjs4hVewaRzJGuT0q8JUKpT26k671enkKeoKgbcEYSM4EexIfqIADKpSqCYzGjzMwni3g+2Oo="
# token = "QgNvWUkSHyLjYXHhCu0w0X08b1rPxP7k7LlWRmLGDGA="
# result = api_client.DES3_decrypt( req_content, api_client.cal_secret(token,crypto_type = "3DES") )
# print( result )

# # Demo 解析返回数据demo
# api_client = APIClient( )
# response = "139X1npaEjmbRd7eid24yuG9IygUX3lkDROwI+OcKAQigon6A3syEL068lx4/Vm9AqulppxOcWkNGWjsQpi9kTRTA6QTLFM+TIWZr33vNkGUNxfN3MR1TdaCr/tDOPxspUXYpoATFU8EpnSG478LwurnH+nBh6FRqhY7u734OqJahj9454kDFZZh4F0qWtETM8I18qOLloaFZ9bd3lnC6Rpp2SFJh7vneAsM9YadzVFyuGSgRemYh6K4fS8AQpkSx0gS3kEShkLxNtapjOSqF9LMWXrFhwRve3KK1XKIfGLRlxx1pJcJ9eBsD8iATKTJ5DjwFxi1ASOqFju7vfg6oqW+pBPBh0BJCC1o1D2W+9d/MhlBKyVxed3eS47HLce75hW7DPUqvXFp00dkpTKAa2QFcjSZXccpPXeHLYSELz0qk5STzPpYWfO2GGPskejzqrFqo6Ii1FEFHtkLQ0mMu7cAEtox8uaLxFF+q4fa8fXeLyTl4OWY7eqW+9AbrPp9/daBKrWRpCw8MhrD+JO3isKCx8kx3CSHPY27CIaxMLw9UpLuzkGLqR2s8wTcAmaEVzqQ/OXRZ3WV4aai6/xedfjNfoJZ3tn2N6rMk1tPjSGZzU4sdi/j1QeBhVjL/nV3rMIPbGDjZV+h4kZejNqeG8GZzpVtIrAm4TrQPT/Mpg1JiQX5YzU6Set37KO5rPto+iZoUuKpXQw="
# token="QgNvWUkSHyLjYXHhCu0w0X08b1rPxP7k7LlWRmLGDGA="
# result = api_client.DES3_decrypt( response, api_client.cal_secret( token , "3DES" ) )
# print(result )

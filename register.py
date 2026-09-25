import requests
from sign import sign

url = 'https://api-h2.tiktokv.com/passport/email/register/v2/?passport-sdk-version=19&iid=7217815534821738246&device_id=7217541768685585926&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=460701&version_name=46.7.1&device_platform=android&ab_version=46.7.1&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=d1faee99c37b7ae8&manifest_version_code=2024607010&resolution=1080*1920&dpi=360&update_version_code=2024607010&_rticket=1680528883739&app_type=normal&sys_region=US&mcc_mnc=26201&timezone_name=America%2FChicago&ts=1680528883&timezone_offset=-21600&build_number=46.7.1&region=US&uoo=0&app_language=en&carrier_region=DE&locale=en&op_region=DE&content_language=he%2C&ac2=wifi&host_abi=armeabi-v7a&cdid=1783efe8-2018-4899-9ca9-20f1f2fae1ea&support_webview=1&okhttp_version=4.1.103.20-tiktok&use_store_region_cookie=1'

email = input("Enter email: ")

password = input("Enter password: ")

data = f'birthday=1990-05-30&email={email}&mix_mode=1&multi_login=1&password={password}'


headers = {
    'accept-encoding': 'gzip',
    'connection': 'Keep-Alive',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'host': 'api-h2.tiktokv.com',
    'multi_login': '1',
    'passport-sdk-version': '19',
    'sdk-version': '2',
    'user-agent': 'com.zhiliaoapp.musically/2022703020 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.12.13.1)',
    #'x-argus'  : 'MvUZ3js4/BLrwIg9bmztL+CK6WgRGzsH40giyrHv77jBLo4tfO0nB28ta09Iw+yIhPce1Ur2UF5Afcuf68wjiQFNCDl7maA15Do+cArySYAZ9RlVuodE8Zw9nHEykwaxm6zT/amCDv0D5zccgqqFj3Khoeb63Zi0GQGusaQWrI60Hi5wPK2ZOAyiOp8sb1tU5HYfGkphab8y6EAQ+kLiwhIslTEy+LlDhEcemxlOyoJ009qBdQtMOjmOW2FQ+2Q2OdxExqQUo3eqKbDfYSxxyjnbFTyipO5AOARmmNpYwqnvnGDeFRKdyw1FvAiJK+SCeauxphO2P/nYjXVu4aalTBagyQl7trT/VthI+sTvO69A4C6sM317IMEUaVtBvWwMpMwtY7Yx/gOASAdLepQSLNVyNZYjaIjmhgpGgw5UDVOsjby4/YQCgmGWOb3QPZq36eM/ZjepF7vrYnZ/wc9zBD3UARxOkLFYhWykKBy2Nq3qeQp5TGyIvuXoCoPIiDV4dnU4BiIfEpJTJiGP+PhAj48e2GbJVPBqake62qIWa8xbCr3BYlC/JfzVVOKZGFqf3qnPzq/Y+PXr7reA956khIvMX1MNFuaBqHHVy42t83L8HQ==',
    #'x-gorgon' : '0404800f40005705dec3089eda4b0a6611b2743fb4765d40e963',
    #'x-khronos : '1680528883',
    #'x-ladon'  : '0Bbgd0nSpSmBykMfIYmpZSKmZCnt7PaEh15zd3mZefpeBPkl',
    'x-bd-client-key': '#x9NIgPcyUbgVZyQLZ/9qAEMNx/Sc6geDRKfb6f3nxvyiynTAOOvQbT8UYfYo36q8wLAYU7wfgBa9JiL/',
    'x-bd-kmsv': '0',
    'x-tt-cmpl-token': 'AgQQAPOhF-RPsLICwaA_el04_khCzDWTv4QaYMj5mg',
    'x-tt-dm-status': 'login=1;ct=1;rt=1',
    'x-tt-multi-sids': '7078584424505836545%3A6b4918689c71ea8d8733319cb2f4935b',
    'x-tt-passport-csrf-token': 'c522e9842b41ed4b389099e36edc0025',
    'x-vc-bdturing-sdk-version': '2.2.1.i18n'
}

# Update cookies
headers['cookie'] = 'passport_csrf_token=eb93cf1bced12e55dbb801b9cd8e38f1; passport_csrf_token_default=eb93cf1bced12e55dbb801b9cd8e38f1; msToken=BPRMxWHw_wFIFRs2zR9y__Nmk_AI_6Qv7lG7FT1S5Jfx9og0VYgUd07Pg-L3Ir92geMjq3wL5FhF8H9RgRrr0twhG70GG5n2WqpqNjo='

headers.update(sign(url.split('?')[1], data))

response = requests.post(url, data=data, headers=headers)

print(response.text)

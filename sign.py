from signer import md5, ladon, argus
from time   import time

def sign(params, data: str or None = None, sec_device_id: str = '', aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = 'v04.04.05-ov-android', sdk_version: int = 134744640, platform: int = 0, unix: int = None):
    x_ss_stub = md5(data.encode()).hexdigest() if data != None else None
    if not unix: unix = int(time())
    return {
        'x-ladon'   : ladon.Ladon.encrypt(unix, license_id, aid),
        'x-argus'   : argus.Argus.get_sign(params, x_ss_stub, unix,
            platform        = platform,
            aid             = aid,
            license_id      = license_id,
            sec_device_id   = sec_device_id,
            sdk_version     = sdk_version_str, 
            sdk_version_int = sdk_version
        ),
        'x-ss-stub' : x_ss_stub.upper()
    }

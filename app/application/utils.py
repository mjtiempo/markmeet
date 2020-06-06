import qrcode
import jwt
from base64 import b64encode
from io import BytesIO

def create_qrcode_str(qrcode_data):
    img = qrcode.make(qrcode_data)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = b64encode(buffered.getvalue())
    return (bytes("data:image/png;base64,", encoding='utf-8') + img_str).decode()

def generate_token(name, email, room, appid, appkey, domain, audience, avatar=None):
    if avatar is None:
        avatar = "https://api.adorable.io/avatars/128/" + email
    payload = {
            "context": {
                "user": {
                    "avatar": avatar,
                    "name": name,
                    "email": email
                },
            },
            "aud": audience,
            "iss": appid,
            "sub": domain,	
            "room": room
        }
    return jwt.encode(payload, appkey, algorithm='HS256').decode()
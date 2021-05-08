import base64

def base64_to_str(x):
    """base64表現を文字列に変換する
    """
    return base64.b64decode(x).decode('utf-8')
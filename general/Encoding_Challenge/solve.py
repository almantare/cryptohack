from pwn import *;from json import loads, dumps;import base64, codecs;from Crypto.Util.number import long_to_bytes

conn = remote("socket.cryptohack.org", 13377)
while True:
	encoded = loads(conn.readline())
	if "flag" not in encoded.keys():
		if encoded['type'] == 'base64':
			decoded = base64.b64decode(encoded['encoded']).decode("ascii")
			print(dumps({"decoded": decoded}))
			conn.sendline(dumps({"decoded": decoded}))
		elif encoded['type'] == 'hex':
			decoded = bytes().fromhex(encoded['encoded']).decode('ascii')
			conn.sendline(dumps({"decoded": decoded}))
		elif encoded['type'] == 'rot13':
			decoded = str(codecs.decode(encoded['encoded'], 'rot_13'))
			print(dumps({"decoded": decoded}))
			conn.sendline(dumps({"decoded": decoded}))
		elif encoded['type'] == 'bigint':
			decoded = long_to_bytes(int(encoded['encoded'], 16)).decode('ascii')
			print(dumps({"decoded": decoded}))
			conn.sendline(dumps({"decoded": decoded}))
		elif encoded['type'] == 'utf-8':
			decoded = "".join(chr(b) for b in encoded['encoded'])
			print(dumps({"decoded": decoded}))
			conn.sendline(dumps({"decoded": decoded}))
	else:
		print(encoded['flag'])
		s = """ __          __  _                               _                _          ____  _      _____                                     
 \ \        / / | |                             | |              | |        / __ \( )    |  __ \                                    
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | |__   __ _  ___| | __    | |  | |/     | |  | |_ __ ___  __ _ _ __ ___   ___ _ __ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | '_ \ / _` |/ __| |/ /    | |  | |      | |  | | '__/ _ \/ _` | '_ ` _ \ / _ \ '__|
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | |_) | (_| | (__|   <     | |__| |      | |__| | | |  __/ (_| | | | | | |  __/ |   
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_.__/ \__,_|\___|_|\_\     \____/       |_____/|_|  \___|\__,_|_| |_| |_|\___|_|"""
		print(s)
		exit()

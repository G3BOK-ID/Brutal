import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
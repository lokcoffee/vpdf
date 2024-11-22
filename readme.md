
encrypt pdf with password
```
$ vpdf --input=${input_unencypted_file} --output={output_file} --encrypt=Y --password=123456
```

decrypt pdf with password
```
$ vpdf --input=${input_encrypted_file} --output={output_file} --encrypt=N --password=123456
```

```
$ py setup.py build
$ vpdf --input=C:\Users\fernando\Desktop\anew\xs.pdf --output=C:\Users\fernando\Desktop\anew\cc.pdf --encrypt=N --password=450345
```
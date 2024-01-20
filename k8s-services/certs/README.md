1. Generate the ec key.
```
openssl ecparam -name prime256v1 -genkey -noout -out key.pem
```
2. Create the root certificate. (Don't foget to add the -extensions)
```
openssl req -new -x509 -out cluster-cert.crt -days 3650 -config ./ca.conf -key key.pem -extensions v3_ca 
```
3. Get the base64 of cert.
```
cat cluster-cert.crt | base64 -w0
```
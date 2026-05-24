import json, urllib.request, urllib.error, sys
payload = {
    "Age": "25-34 years old",
    "EdLevel": "Bachelor's degree (B.A., B.S., B.Eng., etc.)",
    "Employment": "Employed",
    "WorkExp": 5,
    "YearsCode": 8,
    "DevType": "Developer, full-stack",
    "OrgSize": "100 to 499 employees",
    "RemoteWork": "Remote",
    "Industry": "Software Development",
    "Country": "United States",
    "LanguageHaveWorkedWith": "Python;SQL;JavaScript"
}
req = urllib.request.Request('http://127.0.0.1:8000/api/v1/predict', data=json.dumps(payload).encode('utf-8'), headers={'Content-Type':'application/json'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = resp.read().decode('utf-8')
        print('STATUS', resp.status)
        print(body)
except urllib.error.HTTPError as e:
    print('HTTP ERROR', e.code)
    try:
        print(e.read().decode())
    except Exception:
        pass
except Exception as e:
    print('ERR', repr(e))
    sys.exit(1)

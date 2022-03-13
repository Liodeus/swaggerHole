_regex = {
	'google_api'     : r'AIza[0-9A-Za-z-_]{35}',
	'firebase'  : r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
	'google_captcha' : r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
	'google_oauth'   : r'ya29\.[0-9A-Za-z\-_]+',
	'amazon_aws_access_key_id' : r'A[SK]IA[0-9A-Z]{16}',
	'amazon_mws_auth_toke' : r'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
	'amazon_aws_url' : r's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
	'amazon_aws_url2' : r"(" \
		   r"[a-zA-Z0-9-\.\_]+\.s3\.amazonaws\.com" \
		   r"|s3://[a-zA-Z0-9-\.\_]+" \
		   r"|s3-[a-zA-Z0-9-\.\_\/]+" \
		   r"|s3.amazonaws.com/[a-zA-Z0-9-\.\_]+" \
		   r"|s3.console.aws.amazon.com/s3/buckets/[a-zA-Z0-9-\.\_]+)",
	'facebook_access_token' : r'EAACEdEose0cBA[0-9A-Za-z]+',
	'authorization_basic' : r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
	'authorization_bearer' : r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',
	'authorization_api' : r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}',
	'mailgun_api_key' : r'key-[0-9a-zA-Z]{32}',
	'twilio_api_key' : r'SK[0-9a-fA-F]{32}',
	'twilio_account_sid' : r'AC[a-zA-Z0-9_\-]{32}',
	'twilio_app_sid' : r'AP[a-zA-Z0-9_\-]{32}',
	'paypal_braintree_access_token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
	'square_oauth_secret' : r'sq0csp-[ 0-9A-Za-z\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}',
	'square_access_token' : r'sqOatp-[0-9A-Za-z\-_]{22}|EAAA[a-zA-Z0-9]{60}',
	'stripe_standard_api' : r'sk_live_[0-9a-zA-Z]{24}',
	'stripe_restricted_api' : r'rk_live_[0-9a-zA-Z]{24}',
	'github_access_token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
	'rsa_private_key' : r'-----BEGIN RSA PRIVATE KEY-----',
	'ssh_dsa_private_key' : r'-----BEGIN DSA PRIVATE KEY-----',
	'ssh_dc_private_key' : r'-----BEGIN EC PRIVATE KEY-----',
	'pgp_private_block' : r'-----BEGIN PGP PRIVATE KEY BLOCK-----',
	'json_web_token' : r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
	'slack_token' : r"\"api_token\":\"(xox[a-zA-Z]-[a-zA-Z0-9-]+)\"",
	'SSH_privKey' : r"([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)",
	'Heroku API KEY' : r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}',
	'possible_Creds' : r'(?i)(" \
					r"password\s*[`=:\"]+\s*[^\s]+|" \
					r"password is\s*[`=:\"]*\s*[^\s]+|" \
					r"pwd\s*[`=:\"]*\s*[^\s]+|" \
					r"passwd\s*[`=:\"]+\s*[^\s]+)',
	'email': r"[\w\.-]+@[\w\.-]+\.\w+",
	'ip': r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
	'url': r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
}


_domain_to_delete =  [
	"google.",
	"attachment.domain.com",
	"text.domain.com",
	"facbook.",
	"facebook.",
	"attachment.domain.com",
	"linkedin.",
	"twitter.",
	"personal-example.com",
	"example-john-doe.com",
	"example-company.com",
	"apache.org",
	"xxxx.zz",
	"google.fr",
	"example.com",
	"domain.com",
	"viadeo.com",
	"prod.foo.com",
	"dev.foo.com",
	"smartbear.com",
	"url.com",
	"spotify.com",
	"swagger.io",
	"swaggerhub.com",
	"youtube.",
	"youtu.be",
	"reddit.",
	"pinterest.",
	"postman.com",
	"instagram.",
	".acme-corp."
]

_email_to_delete = [
	"@my-company.com",
	"@personal-example.com",
	"@example-company.com",
	"@domain.fr",
	"@email.com",
	"@domain.com",
	"@example.com",
	"help@microsoft.com",
	"@your-company.com"
]


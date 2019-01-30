# banana-bread
A voting system for ranking banana breads in a bake-off competition

## Development

### Requirements

You should have the following installed and running:
* docker
* docker-compose

You should also have Google Cloud OAuth credentials in your environment
variables:
1. Visit https://console.cloud.google.com and log in.
2. Create a new project named however you'd like.
3. Select `APIs&Services` --> `Credentials` from hamburger menu.
4. Select `Create Credentials` --> `OAuth client ID` from dropdown.
5. Select `Web application` radio button.
6. Set `Name` however you like. Under `Authorized JavaScript origins`, add in
http://localhost:5000. Under `Authorized redirect URIs`, add in
http://localhost/oauth2callback.
7. Copy the newly generated client ID and secret values and store them locally
as environment variables called `CLIENT_ID` and `CLIENT_SECRET`.

### Setup

```bash
git clone git@github.com:lekha/banana-bread
cd banana-bread
docker-compose build
docker-compose up
```

Then visit `localhost` from your browser!

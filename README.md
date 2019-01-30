# banana-bread
A voting system for ranking banana breads in a bake-off competition

## Development

### Requirements

You should have the following installed and running:
* docker
* docker-compose

You should also have Google Cloud OAuth credentials:
1. Visit https://console.cloud.google.com and log in.
2. Create a new project named however you'd like.
3. Select `APIs&Services` --> `Credentials` from the hamburger menu.
4. Select `Create Credentials` --> `OAuth client ID` from the dropdown.
5. Select the `Web application` radio button.
6. Set `Name` however you like. Under `Authorized JavaScript origins`, add in
http://localhost:5000. Under `Authorized redirect URIs`, add in
http://localhost/oauth2callback.
7. Copy and store the newly generated client ID and secret values as
`CLIENT_ID` and `CLIENT_SECRET` in the .env file of the project directory.

### Setup

```bash
git clone git@github.com:lekha/banana-bread
cd banana-bread
docker-compose build
docker-compose up
```

Then visit `localhost` from your browser!

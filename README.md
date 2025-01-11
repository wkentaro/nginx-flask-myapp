# zero-to-https-myapp

Zero to (https://)Myapp.

If you don't know how to self-host, you'll be eventually vendor-locked (and pay a high price💰).  
So I explored the minimal setup to host my Flask app at $5/month.  

The full steps from zero to hosting https website.

(hosted at [https://myapp.wkentaro.com](https://myapp.wkentaro.com))

## Full steps (Zero to Myapp)

**0. Server**

I use Ubuntu 24.04 on Linode.

```
# ssh to your linux server
ssh ...

cd /var/www

git clone https://github.com/wkentaro/nginx-flask-myapp.git myapp
```

**1. Flask and Gunicorn**

```
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv
uv sync

uv run gunicorn --bind 0.0.0.0:8000 main:app

# check your app on a browser http://[PUBLIC_IP]:8000
```

**2. Systemctl**

```
cp etc/systemd/system/myapp.service /etc/systemd/system/myapp.service
systemctl start myapp

# check your app on a browser http://[PUBLIC_IP]:8000

# for debugging
systemctl status myapp
journalctl -u myapp
```

**3. Nginx**

```
cp etc/nginx/sites-available/myapp.conf /etc/nginx/sites-available/myapp.conf
ln -s /etc/nginx/sites-available/myapp.conf /etc/nginx/sites-enabled/myapp.conf
systemctl restart nginx

# check your app on a browser at http://myapp.wkentaro.com
```

**4. SSL**

```
snap install --classic certbot
certbot --nginx

# for auto-renewal
systemctl list-timers | grep certbot
```

### References

- [Linode](https://www.linode.com)
- [Gunicorn](https://gunicorn.org/)
- [Nginx](https://www.nginx.com/)
- [Certbot](https://certbot.eff.org/)

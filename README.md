# IdAppointment

Signal a appointment  available at St Herblain city hall on Discord channel

# Need to get ChromeDriver

If you are using Chrome version 105, please download [ChromeDriver 105.0.5195.19](https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.19/)

If you are using Chrome version 104, please download [ChromeDriver 104.0.5112.79](https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/)

If you are using Chrome version 103, please download [ChromeDriver 103.0.5060.134](https://chromedriver.storage.googleapis.com/index.html?path=103.0.5060.134/)


[see more](https://chromedriver.chromium.org/downloads)

# env variable

create .env file
<pre><code>
TOKEN =    token discord BOT <br/>
ID_CHANNEL_PASSWORD =   id discord channel<br/>
PATH_CHROME_DRIVER =   chromedriver PATH<br/>
TIME_TO_TESTING_APPOITMENT =  time to check appoitment seconde<br/>
</code></pre>

# Install
<pre><code>pip install -r  requirements.txt</code></pre>
<pre><code>python appoitment.py</code></pre>

# Args

    -m, --mode  I/i/P/p select id or passport appoitment, default = P

    -b, --browser y/Y/n/N open or not the browser, default = Y

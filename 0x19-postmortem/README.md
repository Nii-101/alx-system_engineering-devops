# Currency Converter Postmorterm Report
In this blog, I share my experience on an error that occured on one of the projects I built for a client, a realtime currency converter.

## Summary and Root cause
About 6 months ago, I was called by my client that his users were seeing a 500 server error anytime they visit the url to do a currency conversion. The root cause was that the provider serving us the exchange rate had changed their API response format. 

## Timeline
- The error was realized on Friday 8th September, 2023 around 1300 hours (GMT) when the users of the website started experiencing 500 server error. 

- I was alerted at 1800 hours GMT. Fortunately I was home and resting so I quickly put the website into maintenance mode.

- I read through the logs and found the errors around 1900 hours GMT.

- I went back to the API provider website to read about the api response parameters and output data which I finished around 2000 hours GMT.

- It took two hours to re-write and test the code.

- Code was pushed to the server at 2200 hours GMT.

- Website was fully back online and working at about 2230 hours GMT.


## Root cause and resolution
The currency converter was built with a laravel backend to fetch the exchange rates every hour from a free provider (of course things subcriptions are not friendly to africans). The project worked fine for about four months until the exchange rate API provider decided to change their response data variables. This meant that the application was referencing and parsing data with undefined variables. 


In fixing the issue, I put the website into maintenance mode and I read through the error logs and noticed _Undefined array index currency_. As if that was the end, there were a couple similar errors as. I had to re-write some portion of the codes especailly the portions that made the API call (parameters had changed) and the portions that parses the API response. Code was pushed back and the website was back online.

## Measures against such problem in future
- Purchase subscripitons of such important API service providers. They usually pre-notify premium users about these changes to their API.
- Trying no to be directly dependent on an API. I could have stored the output of the API in a database and queried it on demand.
- Having a backup service provider to fall on would be a great thing to do.

Nii Odartey E. Lamptey

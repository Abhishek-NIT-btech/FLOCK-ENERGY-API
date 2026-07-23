# Reflection

## What assumptions did you make?

I assumed the portal uses session-based authentication and that authenticated requests require persistent cookies. I also assumed the HTML structure would remain reasonably stable while parsing data.

## Which part was the most difficult?

Understanding the legacy application's request flow and identifying the endpoints that returned structured data instead of HTML.

## If you had another day, what would you improve?

I would implement automatic session renewal, improve parser robustness, add unit tests, and introduce caching for frequently requested data.

## What mistake did you make?

Initially I relied on a browser session while developing. Later I realised a proper automated authentication flow would be more reliable.

## If you were reviewing your own submission, what would you criticise?

I would recommend improving authentication handling and making the HTML parsing more resilient against changes in the portal layout.
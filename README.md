# Lab: JSON Injection

## Outline

Remember, all (most?) JSON is valid Javascript

Reflected/DOM injection
Stored injection

how is eval involved?

What about JSONP? Too much?

Using third party libraries to correctly parse the JSON and prevent injection and execution (like jQuery)

## Resources

- [Client-side JSON injection (reflected DOM-based)](https://portswigger.net/kb/issues/00200371_client-side-json-injection-reflected-dom-based)
- [Client-side JSON injection (stored DOM-based)](https://portswigger.net/kb/issues/00200372_client-side-json-injection-stored-dom-based)
- [StackOverFlow: Injecting javascript in JSON and security](https://stackoverflow.com/questions/6434398/injecting-javascript-in-json-and-security)
- [OWASP: JSON Hijacking](https://www.owasp.org/index.php/AJAX_Security_Cheat_Sheet#Protect_against_JSON_Hijacking_for_Older_Browsers)
- [Server-Side JavaScript Injection](https://media.blackhat.com/bh-us-11/Sullivan/BH_US_11_Sullivan_Server_Side_WP.pdf)
- [Handling Untrusted JSON Safely](https://www.whitehatsec.com/blog/handling-untrusted-json-safely/)
- [Anatomy of a Subtle JSON Vulnerability](https://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx/)
- [Friday the 13th: Attacking JSON - Alvaro Muñoz & Oleksandr Mirosh - AppSecUSA 2017](https://www.youtube.com/watch?v=NqHsaVhlxAQ)
- [The Evil Side of JavaScript: Server-Side JavaScript Injection](https://nvisium.com/blog/2015/08/27/the-evil-side-of-javascript-server-side.html)

## To build locally via Docker Compose:

```
docker-compose up
```
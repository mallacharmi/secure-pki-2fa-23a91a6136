PKI-Based 2FA Microservice
==========================
This project implements a secure Two-Factor Authentication (2FA) microservice using
Public Key Infrastructure (PKI), RSA-4096 key pairs, encrypted seed files, and TOTP.
The microservice runs using Docker and includes scheduled cron-based logging.

----------------------------------------------------------------------
Student Details
----------------------------------------------------------------------
Roll No (Instructor API ID): 23A91A6136
Latest Commit: ba1c657e2e654b174c951b061004915cdcd87d7e

Encrypted Commit Signature:
ZkBIa6cyKZADQy91wf6uumFsWkBVYXdU1KJlyysOzWjCBpDN3xdqzMJlscudFr0xQHHZCiCAz/jgXiynWCbJu3XzE2SkV0avuH/UYOv9u5OrXn7KNs5fbLEDLkle1fGaBXuwEYGEEQSkLaNtGx9KndbLd/s433eab+F8umrFE4KShaS98HiOsRqZMHO1m39NeBLnQrL6nghyULCGFnkDcIPbzcEM2LmtgR9U6ENiHmYHYCiLOVmvPucbBrbWesBUpBM2r06JOeSqXammn8DAKFkOKxyE2z6P250VLTF7aAmULyhjBrdIsUU7YRyDLqZbmamr7/uFoTVahCmTuJi57fxNJJatRna5Ssywq6Q8d5pq3JTpXLYx4ISOTWYhhdy6yoF8rtQ0F9Lf9GxZkx0lc7Nf9ySL4topqi/YJ88WPUtalqLVx3Uzrmts5AcACUnZw2v3MkBzdJzORN7WIdqzx1DtI92/MBNbPrBL9IHQRh8L/GOZxlBu0xAViSPR9Y1psxulJkOzmqUWewZsv7pC/jweyUJS/tlFfZ4e1RrxWiTk/cnE2ndSCY1VUR+UfnA4MAak8iz/yjGCYtTPChh0eag2u9LPjsaVO6IBpC9nQrsFpsAoYaEYkS8XYmKpW8MU4LGxnwLmlpvlE/LDUZR7F3COWo0h03YjjVgv3WJIkXLjCtRM9XCwO/KVdtSxB4g8hE7YaiHNgXR/izBM2LLihJXa9bmH7I0lsnaOPHwQhK2BEW7+BGi8kOBuajoA5Qxn3ty8UHmds7gN+4McwlQ8stzKvIzYelbs+gRHvnX5hS6bx9KVOctt4QTtxYpV7xq+aGwfcGZt0QCrdQdGyXH5R756I0uUxtkexnEr5PJ6JU/CYR88H7/1ZfhdeAblhWmobCEwEWiTgMqIsyAZkl1eaG+k1MfZRAvHaRUT2/jb5EtMkiqxay8cS+vUEkB8ypvczfD5oF8dhmWtzQ4DsofcE/I/47kWAh5FE+Mo7Hq4SIL3oZdr8O4y3oIhhAF0Kpj1oy2ShVOUdWYQFLSk5KObAzeYxdS6kXRy44JVY/4NOoXCa1aB1w3NGBfFv3MFmHHhSIjaK1EB+kk4v0PYh+SaMuoI2CyDk7xEH99Q1yS0kgXPRNXDWmd+JNxQUUNr40fAdnbhAidFp3h2DK+xOt0JKLcg1veqnOhEs1k3dp1i2DQlKu4EClOhfO1V9JcETfFoqOAGZ98cmKzINzjNpwNbsKf/DDpHMrTno57sFGZ9oTzWHcp3g36VxIMddBplBKChO9HxhrcqQbf//TqD00+FU7fc1imn2PqZdhJJtY2UGY8+xqc+e7QqmMmnw1eDPdpc8JdnllVgMAgiIvTuvHyGuA==

Public Key (one line, escaped newlines):
-----BEGIN PUBLIC KEY----- \nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAjQyDq5D+LIn51sBDBVso KpJariK8HKehA4MXTwdkhSCfNS+X7VP814D+wkNIiIdCBGsaVmNmiANy3DzRvgme a3ytMGDf1Bd41X6XURg05nEMgokknQL1acEQe8CwgRdXUr9plAXU1Rpcc5QLZ/Xo lUxvipKSuI/ThdrG7AiYGa4iMfY3krweezA0m2HFGMpqgqxbWPp3QhU7CZPDuq1x Kg/Cr4ZXKi+H5mIwH3I+HfrNJqdrzIIZdMwIu5/x7Ut3hQxZewMw8Zvl2Bh3MxQS 3Q+o/kh9jkPsNFZkwloVaz4MpbnlxPJoyD8HmwStTlTBNhfPtPtj4EmcDMwkD+IP ykJIvsW+TchvAJgzwxu3MNxg/gjbqI2CL8jZmmCNXtUX9nowwLqF+5GCVpC9flnq XTHGrxIXG5SyDrDRIt6AOJgdNmC+55uc1S+Vfx+X7T2rqRMoWpKo4jO8L3nxNzel PdJj1Bkwrl5+kbQA4soCAr51GzdMdWXGDvFXiRxpH9rpH1iZDuCQoljDgKkBftaS D5Qmej5F9A/z0YXlsTGrjOQpMX1ZE8f6nrahrDRtjjIYDPCIR9PYDQMQ8h+XkePl lZLyk6FxuCkbsb/UvdUM3rIAdmYbwZzUat4kdLlJLB0XO9fimM+R4kzptqu1rf9y sRJJiPTcpD8d69sOfq1SgacCAwEAAQ== \n-----END PUBLIC KEY-----

Encrypted Seed:
gpotnKTUjsie5CluxSZGU24ho7QdcQffe1ZqT6g2ABT85/jTscgbjLp10oRdSsZuqoVYkSj8+mYfR6S6Wi74Vvcwg5NPGXBTfptObJgrkG6USid+hHuH6eKOpSp8xYFHORl6DybQee8QMu5w1y4S2qzDP4tjSUF54Dja92X3HEZ3bLHXrEQl02I2SaQ/Iewu0TLEiRvw6fnOBumKCo0QxsQpdR53P3ALJRx6bym5iLR+OGLuTthMPwrPkWSVFhxZX1lPJZNrXJIM6W8lEbJkjJCm/bprgdmwlZvrtklLv9NW/cZIouiQ6omcgy3DX5YmfcjtaK5w1LEts4kTP33qlEz0MWqYOYlJqJuP9dh3sb+iz+54QqcOcXnO66UGVBxv68K/P7CGDOC2YTwTsEiPdyvuNwPiQNPVE7W5Jr/1q0tybc6oLEYy4EVe2LCC/Hfkwo2+tIAs4M4yEsdnnsuwOAnR4hRI1q8hf+2/ZBK7p+3hn6G1Lb7vjfu4hqALLL0c2EJwl6lobGN9H+3qJJwHgjUfxZ+5L+d3kfMD2uYfWQy29bmM2iUEyHzw98yJrxN5tU1/bBD1Eh5Mfc8O670HG9p30vXqHvDS0nTaJQ+mKSczvZ+wL9kB4QP4GnVlFxUlEh/Fk8aK0uZiO63TUjdsLC59RdrmumaZPmfxVwZepes=

----------------------------------------------------------------------
Project Summary
----------------------------------------------------------------------
1. Generate RSA 4096-bit key pair
2. Encrypt the TOTP seed file with the instructor’s public key
3. Sign git commit using student's private key
4. Run the microservice in Docker with persistent storage
5. Provide TOTP verification endpoint
6. Log 2FA validations through a cron job

----------------------------------------------------------------------
Additional Security & Production Hardening
----------------------------------------------------------------------
If deployed to production, the following enhancements MUST be added:

1. Use HSM or KMS for private key storage
2. Enforce HTTPS using TLS 1.3
3. Use Vault/Secrets Manager for seed storage
4. Enable audit logging and SIEM integration
5. Add API rate limiting (e.g., 10 req/min)
6. Add Docker multi-stage builds + non-root user
7. Use Kubernetes with PodSecurity, sealed secrets
8. Enable integrity monitoring for seed + logs
9. Add JWT or OAuth2 authentication in front of API
10. Use fail2ban for brute-force protection

----------------------------------------------------------------------

End of File

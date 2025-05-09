---
theme: bricks
title: aws@localhost
class: text-center
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
---

# aws@localhost

Łukasz Chojnacki | Depcon 15 | 2025-05-09

---
layout: image-right
image: ./img/aws-on-localhost.png
---

# Czym jest localstack?

<ul>
<div v-click><li>narzędzie umożliwiające symulowanie usług chmurowych AWS na lokalnym komputerze</li></div>
<div v-click><li>działa najczęściej w kontenerze Docker</li></div>
</ul>

---

# Dlaczego warto używać localstacka?
<ul>
<div v-click><li>pozwala na lokalne testowanie integracji z usługami AWS</li></div>
<div v-click><li>może być uruchomiony na CI/CD</li></div>
<div v-click><li>redukuje koszty i ryzyko związane z korzystaniem z rzeczywistych usług AWS</li></div>
<div v-click><li>działa w pełni lokalnie, nie wymaga dostępu do internetu</li></div>
<div v-click><li>sprawia, że zespół developerski nie współdzieli zasobów podczas developmentu</li></div>
<div v-click><li>może być konfigurowany takimi samymi narzędziami (Terraform, OpenTofu)</li></div>
</ul>

---
layout: image-right
image: ./img/aws-services.png
---

# Jakie usługi AWS są dostępne?

<ul>
<div v-click>
<li>W wersji darmowej: S3, Lambda, DynamoDB, SQS (Simple Queue Service), SNS (Simple Notification Service)...</li>
</div>
<div v-click>
<li>W wersji Pro: EC2, RDS (Relational Database Service), SES (Simple Email Service), CloudFront...</li>
</div>
</ul>

---
layout: image-right
image: ./img/za-darmo-biere.jpeg
---
# Ile to kosztuje?

<table class="tg"><thead>
  <tr>
    <th><span style="font-weight:bold">Free</span></th>
    <th><span style="font-weight:bold">Basic</span></th>
    <th><span style="font-weight:bold">Ultimate</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td>0$</td>
    <td>$39/month</td>
    <td>$89/month</td>
  </tr>
  <tr>
    <td>30+ usług</td>
    <td>55+ usług</td>
    <td>110+ usług</td>
  </tr>
</tbody>
</table>

---
layout: quote
---
# Disclaimer: aplikacja i wszystkie komendy zostały zvibecodowane z wykorzystaniem JetBrains Junie

---
layout: quote
---
# Demo: Django + S3 storage

---
layout: quote
---
# Demo: Podgląd uruchomionych usług

---
layout: quote
---
# Demo: Django + S3 storage z wersjonowaniem

---
layout: quote
---
# Demo: Django + Celery + SQS

---
layout: quote
---
# Demo: AWS Lambda

---
layout: statement
class: text-center
---
# Dzięki za uwagę!

<div>
<img
  src="./img/any-questions.gif"
  style="margin: auto;"
>
</div>

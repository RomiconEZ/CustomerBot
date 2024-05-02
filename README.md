[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/RomiconEZ/CustomerBot">
    <img src="readme_images/cust-bot-logo.jpg" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">Customer Telegram Bot</h3>
<h3 align="center">(Part of the contact center automation service)</h3>

  <p align="center">
    <br />
    <br />
    <a href="https://github.com/RomiconEZ/CustomerBot/issues">Report Bug</a>
    ·
    <a href="https://github.com/RomiconEZ/CustomerBot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents / Содержание</summary>
  <ol>
    <li>
      <a href="#about-the-project--о-проекте">About The Project / О проекте</a>
      <ul>
        <li><a href="#built-with--технологический-стек">Built With / Технологический стек</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started--начало">Getting Started / Начало</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation--установка">Installation / Установка</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact--контакты">Contact / Контакты</a></li>
  </ol>
</details>




<!-- ABOUT THE PROJECT -->
## About The Project / О проекте

Link to project in GitHub: https://github.com/RomiconEZ/CustomerBot

Данный Telegram Бот является частью системы автоматизации контакт-центра для тур-бизнеса.

Он является связующим звеном между клиентами и агентами тур-бизнеса.

Основные цели бота - отправление текстовых сообщений и звуковых дорожек, сгенерированных на вопрос пользователя; 
сбор отзывов и отправление на Backend сервер;
добавление клиента в очередь ожидания для ответа от агента.

В качестве базы данных для хранения информации о пользователях бота используется PostgreSQL.

Диалоги пользователя с ботом хранятся в Redis. История ограничивается 4 последними сообщениями. 
Также у истории есть максимальный срок хранения - 30 дней.

В данный момент сторонняя аналитика использования бота не используется.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With / Технологический стек

* ![Python][Python.com]
* <img src="readme_images/aiogram_logo.png" alt="lc_ch" style="width:100px; height:auto;">
* ![Docker][Docker.com]
* Init Bot Template: https://github.com/donBarbos/telegram-bot-template


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started / Начало

### Prerequisites
- Docker: https://www.docker.com/get-started

### Installation / Установка

1. Clone the repository.

2. Copy the `.env.example` file in the directory and change the name to `.env`. Customize the env file for your project.

3. Compile locales with a separate command
   ```shell
   pybabel compile -d bot/locales
   ```
4. Launch the Backend Server (https://github.com/RomiconEZ/GenerativeBackend)

5. In the terminal, navigate to the root directory of the cloned repository. Build the Docker containers with the following command:
   ```shell
   docker compose up -d --build
   ```
   Make migrations
   ```shell
   docker compose exec bot alembic upgrade head
   ```

### Additionally
* http://127.0.0.1:3000/ - Grafana

<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact / Контакты

Roman Neronov:
* email: roman.nieronov@gmail.com / roman.nieronov@mail.ru
* telegram: @Romiconchik

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/RomiconEZ/CustomerBot.svg?style=for-the-badge
[contributors-url]: https://github.com/RomiconEZ/CustomerBot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/RomiconEZ/CustomerBot.svg?style=for-the-badge
[forks-url]: https://github.com/RomiconEZ/CustomerBot/network/members
[stars-shield]: https://img.shields.io/github/stars/RomiconEZ/CustomerBot.svg?style=for-the-badge
[stars-url]: https://github.com/RomiconEZ/CustomerBot/stargazers
[issues-shield]: https://img.shields.io/github/issues/RomiconEZ/CustomerBot.svg?style=for-the-badge
[issues-url]: https://github.com/RomiconEZ/CustomerBot/issues
[license-shield]: https://img.shields.io/github/license/RomiconEZ/CustomerBot.svg?style=for-the-badge
[license-url]: https://github.com/RomiconEZ/CustomerBot/blob/master/LICENSE.txt


[Python.com]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white

[Docker.com]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white


# Django E-Learning Platform
### Opis projektu
Platforma e-learningowa stworzona w Django z rozbudowaną funkcjonalnością umożliwiającą:
- Logowanie i zarządzanie użytkownikami.
- Czat dla uczestników kursów z historią zapisywaną w bazie danych, zaimplementowany przy użyciu Django Channels, Redis, ASGI, i WebSocket.
- Dodawanie kursów oraz zapis uczestników na kursy.
- Tworzenie materiałów do kursów w formie:
- Linków do wideo (obsługiwane przez django-embed-video).
- Plików, zdjęć lub tekstów.
- Zarządzanie kursami i treściami przez użytkowników z rolą administratora lub instruktora.
- Cacheowanie danych przy użyciu Redis.
- API stworzone za pomocą Django REST Framework (DRF).
- CMS umożliwiający łatwe zarządzanie treściami platformy.
- Dostęp do kursów przez niestandardowe subdomeny dzięki custom middleware.
### Technologie
Projekt wykorzystuje następujące technologie:
- Django – główny framework aplikacji.
- Daphne – serwer ASGI obsługujący komunikację w czasie rzeczywistym.
- Django REST Framework (DRF) – do budowy API.
- Docker – konteneryzacja aplikacji.
- Redis – jako warstwa cache oraz channel layer dla WebSocket.
- PostgreSQL – baza danych.
- django-embed-video – obsługa osadzania wideo.
- django-debug-toolbar – debugowanie w trybie deweloperskim.
- uWSGI – serwer aplikacji WSGI.
- Nginx – serwer proxy.
- Django Channels – obsługa WebSocket i komunikacji w czasie rzeczywistym.
### Struktura środowisk
Aplikacja posiada trzy różne środowiska:
- base – podstawowa konfiguracja aplikacji.
- local – środowisko deweloperskie.
- prod – środowisko produkcyjne.
### Konteneryzacja
Projekt jest zkonteneryzowany i wykorzystuje:

- **Docker Compose** – do zarządzania kontenerami.
- **Skrypt wait-for-it.sh** – do synchronizacji startu kontenerów.
### Funkcjonalności czatu
- Obsługa czatu w czasie rzeczywistym dla uczestników kursów.
- Historia wiadomości zapisywana w bazie danych.
- Komunikacja oparta na Django Channels, WebSocket, i Redis.

### Instalacja
1. Klonowanie repozytorium:

```git clone -b deploy https://github.com/dmurawski/e-learning-platform.git```

2. Uruchomienie aplikacji:
   
```docker-compose up --build```

3. Migracje bazy danych:
   
```docker-compose exec web python manage.py migrate ```

4. Tworzenie superużytkownika:
   
```docker-compose exec web python manage.py createsuperuser```

### Architektura aplikacji
- **Frontend i backend** obsługiwane przez Nginx jako serwer proxy.
- **Daphne** obsługuje komunikację w czasie rzeczywistym.
- **Redis** pełni rolę kanału komunikacji oraz warstwy cache.
- **PostgreSQL** jako relacyjna baza danych.
- **Docker Compose** ułatwia zarządzanie całym środowiskiem.
### Endpointy
#### API REST
##### SubjectViewSet
  - GET ```/subjects/``` - Lista przedmiotów.
  - GET ```/subjects/<id>/``` - Szczegóły pojedynczego przedmiotu.
##### CourseViewSet
  - GET ```/courses/``` - Lista kursów.
  - GET ```/courses/<id>/``` - Szczegóły pojedynczego kursu.
  - POST ```/courses/<id>/enroll/``` - Lista kursów.
  - GET ```/courses/<id>/contents/``` - Pobranie zawartości kursu (wymaga uwierzytelnienia oraz zapisu na kurs).
#### DJANGO APP


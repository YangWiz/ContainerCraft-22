FROM archlinux:latest

WORKDIR /usr/src/app

COPY pixi.toml .
COPY *.py ./
# Install pixi and install all the requirements.
RUN pacman -Sy pixi --noconfirm
RUN pixi install


EXPOSE 8000

CMD ["pixi", "run", "uvicorn", "main:app"]

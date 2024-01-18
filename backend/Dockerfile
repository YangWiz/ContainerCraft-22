FROM archlinux:latest

WORKDIR /usr/src/app

COPY pixi.toml .

COPY *.py ./

# Install pixi and install all the requirements.
RUN pacman -Sy pixi --noconfirm
RUN pixi install

EXPOSE 2333 

CMD ["pixi", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2333"]

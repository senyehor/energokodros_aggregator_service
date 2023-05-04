FROM --platform=linux/amd64 python:3.11-slim as dependencies-builder
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VERSION '1.2.2'
ENV POETRY_VIRTUALENVS_CREATE false

RUN apt-get update && apt-get install --no-install-recommends -y

RUN pip install --upgrade pip
RUN pip install poetry==$POETRY_VERSION
COPY pyproject.toml ./
# poetry export may take quite a while due to a bug
RUN poetry export --without-hashes --no-interaction \
    --no-ansi -f requirements.txt -o requirements.txt
ENV DEPENDENCIES_DIR /dependencies
RUN pip install --disable-pip-version-check --prefix=$DEPENDENCIES_DIR --no-cache-dir \
    --force-reinstall -r requirements.txt

FROM dependencies-builder as runtime

ENV DEPENDENCIES_DIR /dependencies
ENV APP_DIR /app
RUN mkdir $APP_DIR
RUN mkdir $APP_DIR/staticfiles
WORKDIR $APP_DIR
# copying copliled libs to folder where python expects them to be
COPY --from=dependencies-builder $DEPENDENCIES_DIR /usr/local
# copying app files
COPY . .
RUN rm pyproject.toml
# collecting static and removing develepment staticfiles folder
RUN adduser --system --group --no-create-home app_user
RUN chown -R app_user:app_user $APP_DIR
RUN chmod -R 500 $APP_DIR

USER app_user

CMD ["./docker-entrypoint.sh"]
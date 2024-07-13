ARG BUILD_FROM
FROM $BUILD_FROM

COPY rootfs /
COPY /addons/teleton/homeassistant7.session /

RUN pip install telethon requests
RUN chmod a+x /telethon-to-sensor.py \
    && chmod a+x /run.sh

CMD [ "/run.sh" ]

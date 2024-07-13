ARG BUILD_FROM
FROM $BUILD_FROM

COPY rootfs /

RUN pip install telethon requests
RUN chmod a+x /teleton-to-sensor.py \
    && chmod a+x /run.sh

CMD [ "/run.sh" ]

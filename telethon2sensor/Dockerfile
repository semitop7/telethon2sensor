ARG BUILD_FROM
FROM $BUILD_FROM

COPY rootfs /

RUN pip install telethon==1.36.0 requests==2.32.3
RUN chmod a+x /telethon-to-sensor.py \
    && chmod a+x /run.sh

CMD [ "/run.sh" ]

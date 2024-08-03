ARG BUILD_FROM
FROM $BUILD_FROM

COPY rootfs /

RUN pip install -r requirements.txt
RUN chmod a+x /telethon-to-sensor.py \
    && chmod a+x /run.sh

CMD [ "/run.sh" ]

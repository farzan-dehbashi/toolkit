FROM node:latest
WORKDIR /app
COPY . .
RUN echo "hi"
RUN apt install python3
ENV API_URL=http://google.com
EXPOSE 3000
RUN addgroup mosh2 && useradd -g mosh2 mosh2
CMD ["python3"]


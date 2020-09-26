FROM ubuntu:20.04

# LABEL about the custom image
LABEL maintainer="Andrin Bertschi"
LABEL version="0.1"
LABEL description="trufflephp development image"

ARG DEBIAN_FRONTEND=noninteractive

# run install script
RUN mkdir -p /trufflephp-build
COPY . /trufflephp-build/
WORKDIR /trufflephp-build
RUN chmod +x install-dev-env.sh
RUN /trufflephp-build/install-dev-env.sh

# set up environment vars
ENV JAVA_HOME=/trufflephp-build/graalvm
ENV PATH="/trufflephp-build/graalvm/bin:${PATH}"
ENV trufflephp=/trufflephp-source/trufflephp
ENV TRUFFLEPHP_HOME=/trufflephp-source
ENV TRUFFLEPHP_NATIVE=/trufflephp-source/trufflephp-native/trufflephp-native
ENV TRUFFLEPHP_BUILD_NATIVE=true


# optional alternative environments
RUN /trufflephp-build/install-hhvm.sh
RUN /trufflephp-build/install-jphp.sh
RUN /trufflephp-build/install-php8.sh

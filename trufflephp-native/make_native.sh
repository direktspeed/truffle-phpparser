#!/usr/bin/env bash

# TRUFFLEPHP_BUILD_NATIVE=true

if [[ $TRUFFLEPHP_BUILD_NATIVE == "false" ]]; then
    echo "Skipping the native image build because TRUFFLEPHP_BUILD_NATIVE is set to false."
    exit 0
fi

# install gu if now available

"$JAVA_HOME"/bin/native-image \
    --macro:truffle --no-fallback --initialize-at-build-time \
    -cp ../trufflephp-language/target/trufflephp.jar:../trufflephp-launcher/target/trufflephp-launcher.jar \
    org.trufflephp.launcher.TRUFFLEPHPMain \
    trufflephp-native

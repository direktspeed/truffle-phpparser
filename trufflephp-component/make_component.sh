#!/usr/bin/env bash
cur_dir=$(pwd)
dir="$(dirname "$(readlink -f "$0")")"
cd $dir

readonly JAVA_VERSION="${1}"
echo $JAVA_VERSION
if [[ $JAVA_VERSION == 1.8* ]]; then
    JRE="jre/"
elif [[ $JAVA_VERSION == 11* ]]; then
    JRE=""
else
    echo "Unkown java version: $JAVA_VERSION"
    exit 1
fi
readonly COMPONENT_DIR="component_temp_dir"
readonly LANGUAGE_PATH="$COMPONENT_DIR/$JRE/languages/trufflephp"
if [[ -f ../trufflephp-native/trufflephp-native ]]; then
    echo "including graal native"
    INCLUDE_TRUFFLEPHP_NATIVE="TRUE"
fi

rm -rf COMPONENT_DIR

mkdir -p "$LANGUAGE_PATH"
cp ../trufflephp-language/target/trufflephp.jar "$LANGUAGE_PATH"

mkdir -p "$LANGUAGE_PATH/launcher"
cp ../trufflephp-launcher/target/trufflephp-launcher.jar "$LANGUAGE_PATH/launcher/"

mkdir -p "$LANGUAGE_PATH/bin"
cp ../trufflephp $LANGUAGE_PATH/bin/
if [[ $INCLUDE_TRUFFLEPHP_NATIVE = "TRUE" ]]; then
    echo "including native image"
    cp ../trufflephp-native/trufflephp-native $LANGUAGE_PATH/bin/
fi

touch "$LANGUAGE_PATH/native-image.properties"

mkdir -p "$COMPONENT_DIR/META-INF"
{
    echo "Bundle-Name: Graal PHP";
    echo "Bundle-Symbolic-Name: org.trufflephp";
    echo "Bundle-Version: 20.2.0";
    echo 'Bundle-RequireCapability: org.graalvm; filter:="(&(graalvm_version=20.2.0)(os_arch=amd64))"';
    echo "x-GraalVM-Polyglot-Part: True"
} > "$COMPONENT_DIR/META-INF/MANIFEST.MF"

(
cd $COMPONENT_DIR || exit 1
jar cfm ../trufflephp-component.jar META-INF/MANIFEST.MF .

echo "bin/trufflephp = ../$JRE/languages/trufflephp/bin/trufflephp" > META-INF/symlinks
if [[ $INCLUDE_TRUFFLEPHP_NATIVE = "TRUE" ]]; then
    echo "bin/trufflephp-native = ../$JRE/languages/trufflephp/bin/trufflephp-native" >> META-INF/symlinks
fi
jar uf ../trufflephp-component.jar META-INF/symlinks

{
    echo "$JRE"'languages/trufflephp/bin/trufflephp = rwxrwxr-x'
    echo "$JRE"'languages/trufflephp/bin/trufflephp-native = rwxrwxr-x'
} > META-INF/permissions
jar uf ../trufflephp-component.jar META-INF/permissions
)
rm -rf $COMPONENT_DIR

cd $cur_dir

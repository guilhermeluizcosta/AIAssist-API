#!/usr/bin/env bash
set -o errexit

echo "Instalando requirements gerais..."
pip install -r requirements.txt || exit 1

echo "Instalando sse-starlette isoladamente..."
pip install sse-starlette || exit 1

echo "Build concluído com sucesso."

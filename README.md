# Syndio Backend Test

Demo an API with data read from a sqlite.

## Usage

```sh
pip install git+https://github.com/xsc27/syndio_backend_test.git
export PORT=8000  # Optional: defaults to 5000
python3 -m syndio_backend_test  # Start web server
curl http://127.0.0.1:${PORT}/employees/ | jq .
```

# License

Copyright 2021 Carlos Meza

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

```
 http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

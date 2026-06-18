# Changelog

## 5.1.0 (2026-06-18)

Full Changelog: [v5.0.0...v5.1.0](https://github.com/beeper/desktop-api-python/compare/v5.0.0...v5.1.0)

### Features

* **api:** add app resource with login and verification endpoints ([9868f77](https://github.com/beeper/desktop-api-python/commit/9868f77423a998bfc443bc60fc00d6c7d0e58f53))
* **api:** api update ([9c92ab4](https://github.com/beeper/desktop-api-python/commit/9c92ab490194b4640b4c152e197df698b87d465b))
* **internal/types:** support eagerly validating pydantic iterators ([1850c8a](https://github.com/beeper/desktop-api-python/commit/1850c8a7b7d3e45407524a6ebffe902d4a3f8a71))


### Bug Fixes

* **auth:** prioritize first auth header ([4500314](https://github.com/beeper/desktop-api-python/commit/4500314d39d676c21e20749e1344e0100a5d2b26))
* **client:** add missing f-string prefix in file type error message ([78424e2](https://github.com/beeper/desktop-api-python/commit/78424e24ad4e1f336f843222ff19bf70a50f073f))

## 5.0.0 (2026-05-06)

Full Changelog: [v4.3.0...v5.0.0](https://github.com/beeper/desktop-api-python/compare/v4.3.0...v5.0.0)

### Features

* **api:** add network, bridge fields to accounts ([af70fc9](https://github.com/beeper/desktop-api-python/commit/af70fc9fab45036721b4be634bb4444964c70d1e))
* **api:** api update ([a5afb8f](https://github.com/beeper/desktop-api-python/commit/a5afb8f6a0037bc3727eca0a7ca0c46ca371c6f0))
* **api:** api update ([a1af475](https://github.com/beeper/desktop-api-python/commit/a1af475c4f4c51e2aed27ea8c793364444ed8055))
* **api:** api update ([770a8e2](https://github.com/beeper/desktop-api-python/commit/770a8e2a6fc4d96dae58b3b787d55072faf63e34))
* **api:** manual updates ([c84dca5](https://github.com/beeper/desktop-api-python/commit/c84dca576d56b83e314ab798749607e70aea7223))
* **internal:** implement indices array format for query and form serialization ([de85c3a](https://github.com/beeper/desktop-api-python/commit/de85c3aef481f44350bab667ed81e155573ace81))
* support setting headers via env ([6841539](https://github.com/beeper/desktop-api-python/commit/6841539c8619a507ec5e717d08a81837e83d76c2))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([9e86464](https://github.com/beeper/desktop-api-python/commit/9e86464960e28472bc3a4f137c5d2c025f2acc16))
* **deps:** bump minimum typing-extensions version ([922d90a](https://github.com/beeper/desktop-api-python/commit/922d90aeb6d75306490a359d26ebbf71a6e340b8))
* ensure file data are only sent as 1 parameter ([69f6d11](https://github.com/beeper/desktop-api-python/commit/69f6d11ecb0959d1a5eb90c41c76542a1ea5826f))
* **pydantic:** do not pass `by_alias` unless set ([8b9fe85](https://github.com/beeper/desktop-api-python/commit/8b9fe85df1911bc10a65b5c965e5465c4041e065))
* sanitize endpoint path params ([900c955](https://github.com/beeper/desktop-api-python/commit/900c955edf1d5f8cf7aa9c7d8a7859e5b61ae379))
* use correct field name format for multipart file arrays ([d086e7f](https://github.com/beeper/desktop-api-python/commit/d086e7f0ff86653ace4d1f21c5daf1d6605b3369))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([7addb88](https://github.com/beeper/desktop-api-python/commit/7addb88adf0574857ce646e8a9f15e8eb035a48a))


### Chores

* **ci:** skip lint on metadata-only changes ([1fe013e](https://github.com/beeper/desktop-api-python/commit/1fe013eacfb814508b88eefa3b2ee3bf51618edc))
* **ci:** skip uploading artifacts on stainless-internal branches ([3f5692e](https://github.com/beeper/desktop-api-python/commit/3f5692eb199bd02db1359e8131c8774eee7fabcf))
* configure new SDK language ([8b9d76c](https://github.com/beeper/desktop-api-python/commit/8b9d76c76fe4e3ae99d85429f20d9b782bea2520))
* configure new SDK language ([a54d51a](https://github.com/beeper/desktop-api-python/commit/a54d51a23c31d38e124dc263f748f6ada2f2409c))
* **internal:** add request options to SSE classes ([fcf96d3](https://github.com/beeper/desktop-api-python/commit/fcf96d3c4f3bdbec2cd1b88745cdbbc48e864be2))
* **internal:** codegen related update ([a6b8aac](https://github.com/beeper/desktop-api-python/commit/a6b8aac8430c698cd1a73bab2cd257c9cf553df6))
* **internal:** make `test_proxy_environment_variables` more resilient ([2420dd3](https://github.com/beeper/desktop-api-python/commit/2420dd3d3de95350f142acaf7fb923fd292af59e))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([1ad2ddf](https://github.com/beeper/desktop-api-python/commit/1ad2ddfe678d2a495d69e45d7a1a8f0856af4211))
* **internal:** more robust bootstrap script ([ed8c2c4](https://github.com/beeper/desktop-api-python/commit/ed8c2c499c99ac2f1a4e83054ae0000cb9e12c47))
* **internal:** reformat pyproject.toml ([f11e2a6](https://github.com/beeper/desktop-api-python/commit/f11e2a6c2e25d78bd95e0a81ce52e814dc2a9e79))
* **internal:** tweak CI branches ([311a998](https://github.com/beeper/desktop-api-python/commit/311a998617de99c1defaa4c54f1b8a308d1bfaf3))
* **internal:** update gitignore ([3dfb379](https://github.com/beeper/desktop-api-python/commit/3dfb3799f6ebbde6400db092864361e3b6a6e07f))
* **test:** do not count install time for mock server timeout ([352dc26](https://github.com/beeper/desktop-api-python/commit/352dc26df496dac34b88c8d410a3d5761fad7cde))
* **tests:** bump steady to v0.19.4 ([68f14af](https://github.com/beeper/desktop-api-python/commit/68f14afb85f168eb61a91398165b1d8222fbeea4))
* **tests:** bump steady to v0.19.5 ([9229d32](https://github.com/beeper/desktop-api-python/commit/9229d32b59f8494f49677dbf508d2fedd21cd8b4))
* **tests:** bump steady to v0.19.6 ([166b069](https://github.com/beeper/desktop-api-python/commit/166b069fbd3034b27d16baf50ef96c61a46996d9))
* **tests:** bump steady to v0.19.7 ([31a8e58](https://github.com/beeper/desktop-api-python/commit/31a8e58a09bd798b9930c195da2be239d50a2e77))
* **tests:** bump steady to v0.20.1 ([d2cf119](https://github.com/beeper/desktop-api-python/commit/d2cf119042313a4b82f4a395a43c175874ceca1e))
* **tests:** bump steady to v0.20.2 ([0def55c](https://github.com/beeper/desktop-api-python/commit/0def55c17787849b27d1e8c21cb6cd129069e220))
* **tests:** bump steady to v0.22.1 ([29127f7](https://github.com/beeper/desktop-api-python/commit/29127f7697a10191b913f86e8664321963b55003))
* update placeholder string ([f9883db](https://github.com/beeper/desktop-api-python/commit/f9883db325ccb453c60affa4218f2b257c4d41d8))
* update SDK settings ([b954521](https://github.com/beeper/desktop-api-python/commit/b954521c09743ea77dc1fe3f49e62cadb9cb6b1f))
* update SDK settings ([5df69bf](https://github.com/beeper/desktop-api-python/commit/5df69bf22554340ee0fd0c694fb755c80907ee22))


### Refactors

* **tests:** switch from prism to steady ([ef99778](https://github.com/beeper/desktop-api-python/commit/ef99778f642f49a26aad1d65c59df9f9cfa766e9))

## 4.3.0 (2026-02-20)

Full Changelog: [v4.2.0...v4.3.0](https://github.com/beeper/desktop-api-python/compare/v4.2.0...v4.3.0)

### Features

* **api:** api update ([4f6c268](https://github.com/beeper/desktop-api-python/commit/4f6c2685f00a7fd4f1db0b34faa6e354a0f7e220))
* **api:** api update ([c77412c](https://github.com/beeper/desktop-api-python/commit/c77412c3d4daa460f8901f715a9f59dc1bfa3970))
* **api:** manual updates ([223108d](https://github.com/beeper/desktop-api-python/commit/223108ddc2f84269df96dd8abf6787d8e45c02e6))


### Chores

* update mock server docs ([70593f0](https://github.com/beeper/desktop-api-python/commit/70593f0416d4ed7251957c9fcdb5805e570b2577))
* update SDK settings ([3741b42](https://github.com/beeper/desktop-api-python/commit/3741b42c7ab0c75897bb5cd753b1ce3b323686d2))

## 4.2.0 (2026-02-20)

Full Changelog: [v4.1.296...v4.2.0](https://github.com/beeper/desktop-api-python/compare/v4.1.296...v4.2.0)

### Features

* **api:** add `description` field to chats, make `title` optional ([4ea0387](https://github.com/beeper/desktop-api-python/commit/4ea0387eaec221fd3bbfc38dd0d78bec923a8d81))
* **api:** add reactions ([0af948c](https://github.com/beeper/desktop-api-python/commit/0af948cae96f9ea08c4c60b67a5838c5ef01d731))
* **api:** add upload asset and edit message endpoints ([b73273f](https://github.com/beeper/desktop-api-python/commit/b73273f6831278207d89927097e1cfcfaba7a22a))
* **api:** manual updates ([5693597](https://github.com/beeper/desktop-api-python/commit/56935974d9d28120cb5d69407500b40b4b5a21b5))
* **api:** manual updates ([78862f5](https://github.com/beeper/desktop-api-python/commit/78862f5c997c7b10e46995a163374ee4e85ca935))
* **api:** manual updates ([9e0265f](https://github.com/beeper/desktop-api-python/commit/9e0265f5155064f9c253ed17614e701a13ce39cf))
* **api:** remove mcp for now ([108db8e](https://github.com/beeper/desktop-api-python/commit/108db8e71d02f8457e88f6299597ecad23f756ea))
* **client:** add custom JSON encoder for extended type support ([ee5c367](https://github.com/beeper/desktop-api-python/commit/ee5c36711b7404f9ea30bc90acd3d5406ceec1a7))
* **client:** add support for binary request streaming ([ea509da](https://github.com/beeper/desktop-api-python/commit/ea509daa15ef0e9dcf0b08d379c97dff1b1fd4eb))


### Bug Fixes

* **client:** close streams without requiring full consumption ([5449667](https://github.com/beeper/desktop-api-python/commit/544966767cb709bb67daf01b3e01fc0a1f5b78c8))
* compat with Python 3.14 ([ed03f21](https://github.com/beeper/desktop-api-python/commit/ed03f2168fe6f88ecc7068c8914065784d11561c))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([e185aed](https://github.com/beeper/desktop-api-python/commit/e185aede9d368ba424a73e42e19eafb7ba581222))
* ensure streams are always closed ([3a660be](https://github.com/beeper/desktop-api-python/commit/3a660be67436ef4e2227ed905682c0162fa4ee01))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([9a11f98](https://github.com/beeper/desktop-api-python/commit/9a11f98105b307afcdf27d44a17749908596642c))
* use async_to_httpx_files in patch method ([f37e9db](https://github.com/beeper/desktop-api-python/commit/f37e9db5b52f983f0931cd23182bc4083d135497))


### Chores

* add missing docstrings ([ec4dacb](https://github.com/beeper/desktop-api-python/commit/ec4dacbba523fe8d8c7aa55441f2950de1748f3d))
* add Python 3.14 classifier and testing ([e735dc0](https://github.com/beeper/desktop-api-python/commit/e735dc09e604866003b0dc0acf76c10a1d580f51))
* **ci:** upgrade `actions/github-script` ([c428c2e](https://github.com/beeper/desktop-api-python/commit/c428c2ea4c7abda5a7ba79e5961183c59a4ef2c5))
* configure new SDK language ([df55111](https://github.com/beeper/desktop-api-python/commit/df551116f6eab14028e30d0974b9157a4ed9543d))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([1963ec3](https://github.com/beeper/desktop-api-python/commit/1963ec35e4a9b5aba1dae3533898bad4e8979fb0))
* **docs:** use environment variables for authentication in code snippets ([b8c7ffb](https://github.com/beeper/desktop-api-python/commit/b8c7ffb4b13386fd98afe0ad77ca210320cf3c4b))
* format all `api.md` files ([6897a31](https://github.com/beeper/desktop-api-python/commit/6897a31b748f4e7512ff290c819c86300b265005))
* **internal/tests:** avoid race condition with implicit client cleanup ([3b3c246](https://github.com/beeper/desktop-api-python/commit/3b3c24628854e4fea29e0594ef5ecc31f9444c02))
* **internal:** add `--fix` argument to lint script ([d958469](https://github.com/beeper/desktop-api-python/commit/d95846930fdee434c6aa1f694c84d22e9ec4ea41))
* **internal:** add missing files argument to base client ([85e06b8](https://github.com/beeper/desktop-api-python/commit/85e06b8d715968ffbfaf158ef0e56d468f55bbaa))
* **internal:** bump dependencies ([39b9cbb](https://github.com/beeper/desktop-api-python/commit/39b9cbb70046b145415f3db73f12497cf6446034))
* **internal:** codegen related update ([be5fb2d](https://github.com/beeper/desktop-api-python/commit/be5fb2d9cad77879a2216b770e7bf25ddbe3b778))
* **internal:** fix lint error on Python 3.14 ([fc69586](https://github.com/beeper/desktop-api-python/commit/fc69586dcc697ad18854f6ff6e0e88e6aca00d13))
* **internal:** grammar fix (it's -&gt; its) ([9dd17e2](https://github.com/beeper/desktop-api-python/commit/9dd17e2b322aedd17dc0cd2e5cc78a1ac38ae53a))
* **internal:** update `actions/checkout` version ([d82497d](https://github.com/beeper/desktop-api-python/commit/d82497d40140d08bc2659ef70b1e76e237fb1fa6))
* **package:** drop Python 3.8 support ([3926021](https://github.com/beeper/desktop-api-python/commit/3926021bbdb4c56732364e1b4dc065ec47cf85c0))
* speedup initial import ([78578a1](https://github.com/beeper/desktop-api-python/commit/78578a1910a2cb82650410d82fc9ab6e5099b5e3))
* update lockfile ([366d69a](https://github.com/beeper/desktop-api-python/commit/366d69acd5e42fb975fa2d72002285a6ab76d990))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([cc7035b](https://github.com/beeper/desktop-api-python/commit/cc7035ba857eca0b63dc3c169a43172fe5e2e437))

## 4.1.296 (2025-10-18)

Full Changelog: [v4.1.295...v4.1.296](https://github.com/beeper/desktop-api-python/compare/v4.1.295...v4.1.296)

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([18f66be](https://github.com/beeper/desktop-api-python/commit/18f66bed7a97283166eccdda8832c698aaca6f4a))

## 4.1.295 (2025-10-16)

Full Changelog: [v0.0.1...v4.1.295](https://github.com/beeper/desktop-api-python/compare/v0.0.1...v4.1.295)

### Features

* **api:** bump for new endpoints ([f63e0e4](https://github.com/beeper/desktop-api-python/commit/f63e0e48e35789609f9c589684ab03a9ca97b28d))
* **api:** manual updates ([86218ff](https://github.com/beeper/desktop-api-python/commit/86218ff03f8a0cd42050b0c3babdf78178fda3da))
* **api:** manual updates ([0fcd71f](https://github.com/beeper/desktop-api-python/commit/0fcd71f9951498d349fb816b42dc21347f3ab5dc))
* **api:** manual updates ([dce7124](https://github.com/beeper/desktop-api-python/commit/dce712498ff2678222fd203118e7bb91f13ccfc5))
* **api:** manual updates ([48b4b7f](https://github.com/beeper/desktop-api-python/commit/48b4b7f01064d016b84e954f9aa9f327863cc1d3))
* **api:** manual updates ([c9f3b2d](https://github.com/beeper/desktop-api-python/commit/c9f3b2d3a7fb7e2ce3b30de215497079fff3aca9))
* **api:** manual updates ([7c655fb](https://github.com/beeper/desktop-api-python/commit/7c655fb94ba070083173c15a501be7a0f119a38b))
* **api:** manual updates ([88bce73](https://github.com/beeper/desktop-api-python/commit/88bce73dfef13b6a1cdef0749dc3078af97255e4))
* **api:** manual updates ([1ea87ff](https://github.com/beeper/desktop-api-python/commit/1ea87ff08b4b50541e3c26bef6f4bd581af6324c))
* **api:** manual updates ([b1ba1c0](https://github.com/beeper/desktop-api-python/commit/b1ba1c0584b99ab402f7c1643c13c19881baa600))
* **api:** manual updates ([545ed69](https://github.com/beeper/desktop-api-python/commit/545ed69d7251f47a309f2f46ee4f3b8e4cf1cc60))
* **api:** remove limit from list routes ([d5cb6c2](https://github.com/beeper/desktop-api-python/commit/d5cb6c2ee132bc3d558552df145082396c80521c))


### Chores

* configure new SDK language ([d0b2ca6](https://github.com/beeper/desktop-api-python/commit/d0b2ca6bd2e9331cd42fe5143e0f94861502f11f))
* configure new SDK language ([d11b464](https://github.com/beeper/desktop-api-python/commit/d11b4641e572db6ceb07bb4b9d47b97beadd9253))
* **internal:** detect missing future annotations with ruff ([5e05845](https://github.com/beeper/desktop-api-python/commit/5e058450070fedbd9730bd6ec57fa392974d09e1))
* update SDK settings ([8f54b9a](https://github.com/beeper/desktop-api-python/commit/8f54b9a9ed423fa039b5e59131cd69d7fa809d9e))
* update SDK settings ([0d38dfa](https://github.com/beeper/desktop-api-python/commit/0d38dfa50d797ff879df6d5c633bbcb43c3a98fd))

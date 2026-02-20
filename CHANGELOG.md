# Changelog

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

# Introduction

This spec copied from [Civit.AI wiki](https://github.com/civitai/civitai/wiki/REST-API-Reference) on 12/21/2022.

## Civitai API v1

### Creators
 - [GET /api/v1/creators](#get-apiv1creators)

### Models
 - [GET /api/v1/models](#get-apiv1models)

 ### Model Version
 - [GET /api/v1/model-versions/:modelVersionId](#get-apiv1models-versionsmodelversionid)

### Tags
 - [GET /api/v1/tags](#get-apiv1tags)

### GET /api/v1/creators

#### Endpoint URL

`https://civitai.com/api/v1/creators`

#### Query Parameters

| Name | Type | Description |
|---|---|---|
| limit `(OPTIONAL)` | number | The number of results to be returned per page. This can be a number between 0 and 200. By default, each page will return 20 results. If set to 0, it'll return all the creators |
| page `(OPTIONAL)` | number | The page from which to start fetching creators |
| query `(OPTIONAL)` | string | Search query to filter creators by username |

#### Response Fields

| Name | Type | Description |
|---|---|---|
| username | string | The username of the creator |
| modelCount | number | The amount of models linked to this user |
| link | string | Url to get all models from this user |
| metadata.totalItems | string | The total number of items available |
| metadata.currentPage | string | The the current page you are at |
| metadata.pageSize | string | The the size of the batch |
| metadata.totalPages | string | The total number of pages |
| metadata.nextPage | string | The url to get the next batch of items |
| metadata.prevPage | string | The url to get the previous batch of items |

#### Example

The following example shows a request to get the first 3 model tags from our database:
```sh
curl https://civitai.com/api/v1/creators?limit=3 \
-H "Content-Type: application/json" \
-X GET
```

This would yield the following response:
```json
{
  "items": [
    {
      "username": "Civitai",
      "modelCount": 848,
      "link": "https://civitai.com/api/v1/models?username=Civitai"
    },
    {
      "username": "JustMaier",
      "modelCount": 8,
      "link": "https://civitai.com/api/v1/models?username=JustMaier"
    },
    {
      "username": "maxhulker",
      "modelCount": 2,
      "link": "https://civitai.com/api/v1/models?username=maxhulker"
    }
  ],
  "metadata": {
    "totalItems": 46,
    "currentPage": 1,
    "pageSize": 3,
    "totalPages": 16,
    "nextPage": "https://civitai.com/api/v1/creators?limit=3&page=2"
  }
}
```

### GET /api/v1/models

#### Endpoint URL

`https://civitai.com/api/v1/models`

#### Query Parameters

| Name | Type | Description |
|---|---|---|
| limit `(OPTIONAL)` | number | The number of results to be returned per page. This can be a number between 1 and 200. By default, each page will return 100 results |
| page `(OPTIONAL)` | number | The page from which to start fetching models |
| query `(OPTIONAL)` | string | Search query to filter models by name |
| tag `(OPTIONAL)` | string | Search query to filter models by tag |
| username `(OPTIONAL)` | string | Search query to filter models by user |
| types `(OPTIONAL)` | enum `(Checkpoint, TextualInversion, Hypernetwork, AestheticGradient)` | The type of model you want to filter with. If none is specified, it will return all types |
| sort `(OPTIONAL)` | enum `(Highest Rated, Most Downloaded, Newest)` | The order in which you wish to sort the results |
| period `(OPTIONAL)`| enum `(AllTime, Year, Month, Week, Day)` | The time frame in which the models will be sorted |
| rating `(OPTIONAL)` | number | The rating you wish to filter the models with. If none is specified, it will return models with any rating |

#### Response Fields

| Name | Type | Description |
|---|---|---|
| id | number | The identifier for the model |
| name | string | The name of the model |
| description | string | The description of the model (HTML) |
| type | enum `(Checkpoint, TextualInversion, Hypernetwork, AestheticGradient)` | The model type |
| nsfw | boolean | Whether the model is NSFW or not |
| tags| string[] | The tags associated with the model |
| creator.username | string | The name of the creator |
| creator.image | string \| null | The url of the creators avatar |
| modelVersions.id | number | The identifier for the model version |
| modelVersions.name | string | The name of the model version |
| modelVersions.createdAt | Date | The date in which the version was created |
| modelVersions.downloadUrl | string | The download url to get the model file for this specific version |
| modelVersions.trainedWords | string[] | The words used to trigger the model |
| modelVersions.files.sizeKb | number | The size of the model file |
| modelVersions.files.format | string | The format of the file ('pickle' or 'safetensor') |
| modelVersions.files.pickleScanResult | string | Status of the pickle scan ('Pending', 'Success', 'Danger', 'Error') |
| modelVersions.files.virusScanResult | string | Status of the virus scan ('Pending', 'Success', 'Danger', 'Error') |
| modelVersions.files.scannedAt | Date \| null | The date in which the file was scanned |
| modelVersions.images.url | string | The url for the image |
| modelVersions.images.nsfw | string | Whether or not the image is NSFW (note: if the model is NSFW, treat all images on the model as NSFW) |
| modelVersions.images.width | number | The original width of the image |
| modelVersions.images.height | number | The original height of the image |
| modelVersions.images.hash | string | The [blurhash](https://blurha.sh/) of the image |
| modelVersions.images.meta | object \| null | The generation params of the image |
| metadata.totalItems | string | The total number of items available |
| metadata.currentPage | string | The the current page you are at |
| metadata.pageSize | string | The the size of the batch |
| metadata.totalPages | string | The total number of pages |
| metadata.nextPage | string | The url to get the next batch of items |
| metadata.prevPage | string | The url to get the previous batch of items |

**Note:** The download url uses a `content-disposition` header to set the filename correctly. Be sure to enable that header when fetching the download. For example, with `wget`:
```
wget https://civitai.com/api/download/models/{modelVersionId} --content-disposition
```

#### Example

The following example shows a request to get the first 3 `Textual Inversion` models from our database:
```sh
curl https://civitai.com/api/v1/models?limit=3&type=TextualInversion \
-H "Content-Type: application/json" \
-X GET
```

This would yield the following response:
```json
{
  "items": [
    {
      "id": 64,
      "name": "Redshift Diffusion",
      "type": "Checkpoint",
      "nsfw": false,
      "tags": [
        "render",
        "3d",
        "style"
      ],
      "modelVersions": [
        {
          "id": 73,
          "name": "v1",
          "createdAt": "2022-11-13T02:43:39.839Z",
          "trainedWords": [
            "redshift style"
          ],
          "downloadUrl": "https://civitai.com/api/download/models/73"
        }
      ]
    },
    {
      "id": 23,
      "name": "Arcane Diffusion",
      "type": "Checkpoint",
      "nsfw": false,
      "tags": [
        "style",
        "Anime",
        "Arcane",
        "League of Legends ",
        "nitrosocke"
      ],
      "modelVersions": [
        {
          "id": 23,
          "name": "V1",
          "createdAt": "2022-11-04T19:41:24.643Z",
          "trainedWords": [
            "arcane style"
          ],
          "downloadUrl": "https://civitai.com/api/download/models/23"
        },
        {
          "id": 25,
          "name": "V3",
          "createdAt": "2022-11-04T19:45:47.336Z",
          "trainedWords": [
            "arcane style"
          ],
          "downloadUrl": "https://civitai.com/api/download/models/25"
        },
        {
          "id": 24,
          "name": "V2",
          "createdAt": "2022-11-04T19:42:47.336Z",
          "trainedWords": [
            "arcane style"
          ],
          "downloadUrl": "https://civitai.com/api/download/models/24"
        }
      ]
    },
    {
      "id": 1087,
      "name": "Inkpunk Diffusion",
      "type": "Checkpoint",
      "nsfw": false,
      "tags": [
        "style",
        "illustration",
        "Yoji Shinkawa",
        "flcl",
        "gorillaz",
        "punk"
      ],
      "modelVersions": [
        {
          "id": 1138,
          "name": "v2",
          "createdAt": "2022-11-28T20:32:37.237Z",
          "trainedWords": [
            "nvinkpunk"
          ],
          "downloadUrl": "https://civitai.com/api/download/models/1138"
        },
        {
          "id": 1087,
          "name": "v1",
          "createdAt": "2022-11-25T16:47:49.287Z",
          "trainedWords": [
            "nvinkpunk"
          ],
          "downloadUrl": "https://civitai.com/api/download/models/1087"
        }
      ]
    }
  ],
  "metadata": {
    "totalItems": 967,
    "currentPage": 1,
    "pageSize": 3,
    "totalPages": 323,
    "nextPage": "https://civitai.com/api/v1/models?limit=3&type=TextualInversion&page=2"
  }
}
```

### GET /api/v1/models-versions/:modelVersionId

#### Endpoint URL

`https://civitai.com/api/v1/model-versions/:id`

#### Response Fields

| Name | Type | Description |
|---|---|---|
| id | number | The identifier for the model version |
| name | string | The name of the model version |
| model.name | string | The name of the model |
| model.type | enum `(Checkpoint, TextualInversion, Hypernetwork, AestheticGradient)` | The model type |
| model.nsfw | boolean | Whether the model is NSFW or not |
| model.poi | boolean | Whether the model is of a person of interest or not |
| modelId | number | The identifier for the model |
| createdAt | Date | The date in which the version was created |
| downloadUrl | string | The download url to get the model file for this specific version |
| trainedWords | string[] | The words used to trigger the model |
| files.sizeKb | number | The size of the model file |
| files.format | string | The format of the file ('pickle' or 'safetensor') |
| files.pickleScanResult | string | Status of the pickle scan ('Pending', 'Success', 'Danger', 'Error') |
| files.virusScanResult | string | Status of the virus scan ('Pending', 'Success', 'Danger', 'Error') |
| files.scannedAt | Date \| null | The date in which the file was scanned |
| images.url | string | The url for the image |
| images.nsfw | string | Whether or not the image is NSFW (note: if the model is NSFW, treat all images on the model as NSFW) |
| images.width | number | The original width of the image |
| images.height | number | The original height of the image |
| images.hash | string | The [blurhash](https://blurha.sh/) of the image |
| images.meta | object \| null | The generation params of the image |

**Note:** The download url uses a `content-disposition` header to set the filename correctly. Be sure to enable that header when fetching the download. For example, with `wget`:
```
wget https://civitai.com/api/download/models/{modelVersionId} --content-disposition
```

#### Example

The following example shows a request to get a model version from our database:
```sh
curl https://civitai.com/api/v1/modelVersions/1318 \
-H "Content-Type: application/json" \
-X GET
```

This would yield the following response:
```json
{
  "id": 1318,
  "name": "toad",
  "createdAt": "2022-12-08T19:58:49.765Z",
  "updatedAt": "2022-12-08T20:24:50.330Z",
  "trainedWords": [
    "ttdddd"
  ],
  "modelId": 1244,
  "modelName": "froggy style",
  "files": [
    {
      "sizeKB": 2546414.971679688,
      "format": "PickleTensor",
      "pickleScanResult": "Success",
      "pickleScanMessage": "**Detected Pickle imports (3)**\n```\ncollections.OrderedDict\ntorch.HalfStorage\ntorch._utils._rebuild_tensor_v2\n```",
      "virusScanResult": "Success",
      "scannedAt": "2022-12-08T20:15:36.133Z"
    }
  ],
  "images": [
    {
      "url": "https://imagecache.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/c6ed4a9d-ae75-463b-7762-da0455cc5700/width=450",
      "nsfw": false,
      "width": 832,
      "height": 832,
      "hash": "U8Civ__MTeSP?utJ9IDj?^Ek=}RQyEE1-Vr=",
      "meta": null
    },
    {
      "url": "https://imagecache.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/ed1af033-e944-49ae-5957-f516710f8c00/width=450",
      "nsfw": false,
      "width": 1024,
      "height": 1024,
      "hash": "UMECq1DkIoMy_LIVD+Rk-oRjMytRslWBoeoe",
      "meta": null
    }
  ],
  "downloadUrl": "https://civitai.com/api/download/models/1318"
}
```


### GET /api/v1/tags

#### Endpoint URL

`https://civitai.com/api/v1/tags`

#### Query Parameters

| Name | Type | Description |
|---|---|---|
| limit `(OPTIONAL)` | number | The number of results to be returned per page. This can be a number between 1 and 200. By default, each page will return 20 results. If set to 0, it'll return all the tags |
| page `(OPTIONAL)` | number | The page from which to start fetching tags |
| query `(OPTIONAL)` | string | Search query to filter tags by name |

#### Response Fields

| Name | Type | Description |
|---|---|---|
| name | string | The name of the tag |
| modelCount | number | The amount of models linked to this tag |
| link | string | Url to get all models from this tag |
| metadata.totalItems | string | The total number of items available |
| metadata.currentPage | string | The the current page you are at |
| metadata.pageSize | string | The the size of the batch |
| metadata.totalPages | string | The total number of pages |
| metadata.nextPage | string | The url to get the next batch of items |
| metadata.prevPage | string | The url to get the previous batch of items |

#### Example

The following example shows a request to get the first 3 model tags from our database:
```sh
curl https://civitai.com/api/v1/tags?limit=3 \
-H "Content-Type: application/json" \
-X GET
```

This would yield the following response:
```json
{
  "items": [
    {
      "name": "Pepe Larraz",
      "modelCount": 1,
      "link": "https://civitai.com/api/v1/models?tag=Pepe Larraz"
    },
    {
      "name": "comic book",
      "modelCount": 7,
      "link": "https://civitai.com/api/v1/models?tag=comic book"
    },
    {
      "name": "style",
      "modelCount": 91,
      "link": "https://civitai.com/api/v1/models?tag=style"
    }
  ],
  "metadata": {
    "totalItems": 200,
    "currentPage": 1,
    "pageSize": 3,
    "totalPages": 67,
    "nextPage": "https://civitai.com/api/v1/tags?limit=3&page=2"
  }
}
```
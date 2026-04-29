# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import asset_serve_params, asset_upload_params, asset_download_params, asset_upload_base64_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.asset_upload_response import AssetUploadResponse
from ..types.asset_download_response import AssetDownloadResponse
from ..types.asset_upload_base64_response import AssetUploadBase64Response

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    """Manage assets in Beeper Desktop, like message attachments"""

    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def download(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetDownloadResponse:
        """
        Download a Matrix asset using its mxc:// or localmxc:// URL to the device
        running Beeper Desktop and return the local file URL.

        Args:
          url: Matrix content URL (mxc:// or localmxc://) for the asset to download.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/assets/download",
            body=maybe_transform({"url": url}, asset_download_params.AssetDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDownloadResponse,
        )

    def serve(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Stream a file given an mxc://, localmxc://, or file:// URL.

        Downloads first if
        not cached. Supports Range requests for seeking in large files.

        Args:
          url: Asset URL to serve. Accepts mxc://, localmxc://, or file:// URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            "/v1/assets/serve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, asset_serve_params.AssetServeParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        file_name: str | Omit = omit,
        mime_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadResponse:
        """Upload a file to a temporary location using multipart/form-data.

        Returns an
        uploadID that can be referenced when sending messages with attachments.

        Args:
          file: The file to upload (max 500 MB).

          file_name: Original filename. Defaults to the uploaded file name if omitted

          mime_type: MIME type. Auto-detected from magic bytes if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "file_name": file_name,
                "mime_type": mime_type,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/assets/upload",
            body=maybe_transform(body, asset_upload_params.AssetUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadResponse,
        )

    def upload_base64(
        self,
        *,
        content: str,
        file_name: str | Omit = omit,
        mime_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadBase64Response:
        """Upload a file using a JSON body with base64-encoded content.

        Returns an uploadID
        that can be referenced when sending messages with attachments. Alternative to
        the multipart upload endpoint.

        Args:
          content: Base64-encoded file content (max ~500MB decoded)

          file_name: Original filename. Generated if omitted

          mime_type: MIME type. Auto-detected from magic bytes if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/assets/upload/base64",
            body=maybe_transform(
                {
                    "content": content,
                    "file_name": file_name,
                    "mime_type": mime_type,
                },
                asset_upload_base64_params.AssetUploadBase64Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadBase64Response,
        )


class AsyncAssetsResource(AsyncAPIResource):
    """Manage assets in Beeper Desktop, like message attachments"""

    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/beeper/desktop-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/beeper/desktop-api-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def download(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetDownloadResponse:
        """
        Download a Matrix asset using its mxc:// or localmxc:// URL to the device
        running Beeper Desktop and return the local file URL.

        Args:
          url: Matrix content URL (mxc:// or localmxc://) for the asset to download.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/assets/download",
            body=await async_maybe_transform({"url": url}, asset_download_params.AssetDownloadParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetDownloadResponse,
        )

    async def serve(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Stream a file given an mxc://, localmxc://, or file:// URL.

        Downloads first if
        not cached. Supports Range requests for seeking in large files.

        Args:
          url: Asset URL to serve. Accepts mxc://, localmxc://, or file:// URLs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            "/v1/assets/serve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url": url}, asset_serve_params.AssetServeParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        file_name: str | Omit = omit,
        mime_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadResponse:
        """Upload a file to a temporary location using multipart/form-data.

        Returns an
        uploadID that can be referenced when sending messages with attachments.

        Args:
          file: The file to upload (max 500 MB).

          file_name: Original filename. Defaults to the uploaded file name if omitted

          mime_type: MIME type. Auto-detected from magic bytes if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "file": file,
                "file_name": file_name,
                "mime_type": mime_type,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/assets/upload",
            body=await async_maybe_transform(body, asset_upload_params.AssetUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadResponse,
        )

    async def upload_base64(
        self,
        *,
        content: str,
        file_name: str | Omit = omit,
        mime_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetUploadBase64Response:
        """Upload a file using a JSON body with base64-encoded content.

        Returns an uploadID
        that can be referenced when sending messages with attachments. Alternative to
        the multipart upload endpoint.

        Args:
          content: Base64-encoded file content (max ~500MB decoded)

          file_name: Original filename. Generated if omitted

          mime_type: MIME type. Auto-detected from magic bytes if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/assets/upload/base64",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "file_name": file_name,
                    "mime_type": mime_type,
                },
                asset_upload_base64_params.AssetUploadBase64Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetUploadBase64Response,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.download = to_raw_response_wrapper(
            assets.download,
        )
        self.serve = to_custom_raw_response_wrapper(
            assets.serve,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            assets.upload,
        )
        self.upload_base64 = to_raw_response_wrapper(
            assets.upload_base64,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.download = async_to_raw_response_wrapper(
            assets.download,
        )
        self.serve = async_to_custom_raw_response_wrapper(
            assets.serve,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            assets.upload,
        )
        self.upload_base64 = async_to_raw_response_wrapper(
            assets.upload_base64,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.download = to_streamed_response_wrapper(
            assets.download,
        )
        self.serve = to_custom_streamed_response_wrapper(
            assets.serve,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            assets.upload,
        )
        self.upload_base64 = to_streamed_response_wrapper(
            assets.upload_base64,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.download = async_to_streamed_response_wrapper(
            assets.download,
        )
        self.serve = async_to_custom_streamed_response_wrapper(
            assets.serve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            assets.upload,
        )
        self.upload_base64 = async_to_streamed_response_wrapper(
            assets.upload_base64,
        )

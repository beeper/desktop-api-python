# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import asset_upload_params, asset_download_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.asset_upload_response import AssetUploadResponse
from ..types.asset_download_response import AssetDownloadResponse

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

    def upload(
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
    ) -> AssetUploadResponse:
        """Upload a file to a temporary location.

        Supports JSON body with base64 `content`
        field, or multipart/form-data with `file` field. Returns a local file URL that
        can be used when sending messages with attachments.

        Args:
          content: Base64-encoded file content (max ~500MB decoded)

          file_name: Original filename. Generated if omitted

          mime_type: MIME type. Auto-detected from magic bytes if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "content": content,
                "file_name": file_name,
                "mime_type": mime_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
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

    async def upload(
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
    ) -> AssetUploadResponse:
        """Upload a file to a temporary location.

        Supports JSON body with base64 `content`
        field, or multipart/form-data with `file` field. Returns a local file URL that
        can be used when sending messages with attachments.

        Args:
          content: Base64-encoded file content (max ~500MB decoded)

          file_name: Original filename. Generated if omitted

          mime_type: MIME type. Auto-detected from magic bytes if omitted

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "content": content,
                "file_name": file_name,
                "mime_type": mime_type,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
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


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.download = to_raw_response_wrapper(
            assets.download,
        )
        self.upload = to_raw_response_wrapper(
            assets.upload,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.download = async_to_raw_response_wrapper(
            assets.download,
        )
        self.upload = async_to_raw_response_wrapper(
            assets.upload,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.download = to_streamed_response_wrapper(
            assets.download,
        )
        self.upload = to_streamed_response_wrapper(
            assets.upload,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.download = async_to_streamed_response_wrapper(
            assets.download,
        )
        self.upload = async_to_streamed_response_wrapper(
            assets.upload,
        )

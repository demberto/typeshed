import datetime
import sys
from collections.abc import Callable, Mapping
from typing import Any, Literal, NamedTuple, Protocol, TypedDict
from typing_extensions import TypeAlias

CEF_COLOR_TYPE_RGBA_8888: int = ...
CEF_COLOR_TYPE_BGRA_8888: int = ...

CEF_ALPHA_TYPE_OPAQUE: int = ...
CEF_ALPHA_TYPE_PREMULTIPLIED: int = ...
CEF_ALPHA_TYPE_POSTMULTIPLIED: int = ...

DRAG_OPERATION_NONE: int = ...
DRAG_OPERATION_COPY: int = ...
DRAG_OPERATION_LINK: int = ...
DRAG_OPERATION_GENERIC: int = ...
DRAG_OPERATION_PRIVATE: int = ...
DRAG_OPERATION_MOVE: int = ...
DRAG_OPERATION_DELETE: int = ...
DRAG_OPERATION_EVERY: int = ...

NetworkError: TypeAlias = int
ERR_NONE: int = ...
ERR_ABORTED: int = ...
ERR_ACCESS_DENIED: int = ...
ERR_ADDRESS_INVALID: int = ...
ERR_ADDRESS_UNREACHABLE: int = ...
ERR_CACHE_MISS: int = ...
ERR_CERT_AUTHORITY_INVALID: int = ...
ERR_CERT_COMMON_NAME_INVALID: int = ...
ERR_CERT_CONTAINS_ERRORS: int = ...
ERR_CERT_DATE_INVALID: int = ...
ERR_CERT_END: int = ...
ERR_CERT_INVALID: int = ...
ERR_CERT_NO_REVOCATION_MECHANISM: int = ...
ERR_CERT_REVOKED: int = ...
ERR_CERT_UNABLE_TO_CHECK_REVOCATION: int = ...
ERR_CONNECTION_ABORTED: int = ...
ERR_CONNECTION_CLOSED: int = ...
ERR_CONNECTION_FAILED: int = ...
ERR_CONNECTION_REFUSED: int = ...
ERR_CONNECTION_RESET: int = ...
ERR_DISALLOWED_URL_SCHEME: int = ...
ERR_EMPTY_RESPONSE: int = ...
ERR_FAILED: int = ...
ERR_FILE_NOT_FOUND: int = ...
ERR_FILE_TOO_BIG: int = ...
ERR_INSECURE_RESPONSE: int = ...
ERR_INTERNET_DISCONNECTED: int = ...
ERR_INVALID_ARGUMENT: int = ...
ERR_INVALID_CHUNKED_ENCODING: int = ...
ERR_INVALID_HANDLE: int = ...
ERR_INVALID_RESPONSE: int = ...
ERR_INVALID_URL: int = ...
ERR_METHOD_NOT_SUPPORTED: int = ...
ERR_NAME_NOT_RESOLVED: int = ...
ERR_NO_SSL_VERSIONS_ENABLED: int = ...
ERR_NOT_IMPLEMENTED: int = ...
ERR_RESPONSE_HEADERS_TOO_BIG: int = ...
ERR_SSL_CLIENT_AUTH_CERT_NEEDED: int = ...
ERR_SSL_PROTOCOL_ERROR: int = ...
ERR_SSL_RENEGOTIATION_REQUESTED: int = ...
ERR_SSL_VERSION_OR_CIPHER_MISMATCH: int = ...
ERR_TIMED_OUT: int = ...
ERR_TOO_MANY_REDIRECTS: int = ...
ERR_TUNNEL_CONNECTION_FAILED: int = ...
ERR_UNEXPECTED: int = ...
ERR_UNEXPECTED_PROXY_AUTH: int = ...
ERR_UNKNOWN_URL_SCHEME: int = ...
ERR_UNSAFE_PORT: int = ...
ERR_UNSAFE_REDIRECT: int = ...

FOCUS_SOURCE_NAVIGATION: int = ...
FOCUS_SOURCE_SYSTEM: int = ...

JSDIALOGTYPE_ALERT: int = ...
JSDIALOGTYPE_CONFIRM: int = ...
JSDIALOGTYPE_PROMPT: int = ...

KeyEventType: TypeAlias = int
KEYEVENT_RAWKEYDOWN: int = ...
KEYEVENT_KEYDOWN: int = ...
KEYEVENT_KEYUP: int = ...
KEYEVENT_CHAR: int = ...

KeyEventFlags: TypeAlias = int
EVENTFLAG_NONE: int = ...
EVENTFLAG_CAPS_LOCK_ON: int = ...
EVENTFLAG_SHIFT_DOWN: int = ...
EVENTFLAG_CONTROL_DOWN: int = ...
EVENTFLAG_ALT_DOWN: int = ...
EVENTFLAG_LEFT_MOUSE_BUTTON: int = ...
EVENTFLAG_MIDDLE_MOUSE_BUTTON: int = ...
EVENTFLAG_RIGHT_MOUSE_BUTTON: int = ...
if sys.platform == "darwin":
    EVENTFLAG_COMMAND_DOWN: int = ...
    EVENTFLAG_NUM_LOCK_ON: int = ...
    EVENTFLAG_IS_KEY_PAD: int = ...
    EVENTFLAG_IS_LEFT: int = ...
    EVENTFLAG_IS_RIGHT: int = ...

LOGSEVERITY_VERBOSE: int = ...
LOGSEVERITY_INFO: int = ...
LOGSEVERITY_WARNING: int = ...
LOGSEVERITY_ERROR: int = ...
LOGSEVERITY_DISABLE: int = ...

STATE_DEFAULT: int = ...
STATE_ENABLED: int = ...
STATE_DISABLED: int = ...

PaintElementType: TypeAlias = int
PET_VIEW: int = ...
PET_POPUP: int = ...

TID_UI: int = ...
TID_FILE: int = ...
TID_FILE_BACKGROUND: int = ...
TID_FILE_USER_VISIBLE: int = ...
TID_FILE_USER_BLOCKING: int = ...
TID_IO: int = ...
TID_RENDERER: int = ...

TerminationStatus: TypeAlias = int
TS_ABNORMAL_TERMINATION: int = ...
TS_PROCESS_WAS_KILLED: int = ...
TS_PROCESS_CRASHED: int = ...

WindowOpenDisposition: TypeAlias = int
WOD_UNKNOWN: int = ...
WOD_CURRENT_TAB: int = ...
WOD_SINGLETON_TAB: int = ...
WOD_NEW_FOREGROUND_TAB: int = ...
WOD_NEW_BACKGROUND_TAB: int = ...
WOD_NEW_POPUP: int = ...
WOD_NEW_WINDOW: int = ...
WOD_SAVE_TO_DISK: int = ...
WOD_OFF_THE_RECORD: int = ...
WOD_IGNORE_ACTION: int = ...

def CreateBrowserSync(
    window_info: WindowInfo | None = ...,
    settings: BrowserSettings | None = ...,
    url: str | None = ...,
    window_title: str | None = ...,
) -> Browser: ...
def GetAppSetting(key: str) -> object: ...
def GetApp(file_: str | None = ...) -> str: ...
def GetBrowserByIdentifier(identifier: int) -> None: ...
def GetBrowserByWindowHandle(windowHandle: int) -> None: ...
def GetCommandLineSwitch(key: str) -> object: ...
def GetDataUrl(data: str, mediaType: Literal["html"] = "html") -> object: ...
def GetGlobalClientCallback(name: str) -> Callable[..., None]: ...
def GetModuleDirectory() -> str: ...
def GetVersion() -> _Version: ...
def Initialize(settings: ApplicationSettings | None = ..., switches: Mapping[str, Any] | None = ...) -> bool: ...
def IsThread(threadID: int) -> bool: ...
def LoadCrlSetsFile(path: bytes) -> bool: ...
def MessageLoop() -> None: ...
def MessageLoopWork() -> None: ...
def PostTask(thread: int, func: Callable[..., None], *args: _JSValue) -> None: ...
def PostDelayedTask(thread: int, delay_ms: int, func: Callable[..., None], *args: _JSValue) -> None: ...
def QuitMessageLoop() -> None: ...
def SetGlobalClientCallback(name: str, callback: Callable[..., None]) -> None: ...
def SetGlobalClientHandler(handler: object) -> None: ...
def SetOsModalLoop(modalLoop: bool) -> None: ...
def Shutdown() -> None: ...

class ApplicationSettings(TypedDict):
    accept_language_list: str
    app_user_model_id: str
    auto_zooming: str
    background_color: int
    browser_subprocess_path: str
    cache_path: str
    command_line_args_disabled: bool
    context_menu: _ContextMenuOptions
    downloads_enabled: bool
    external_message_pump: bool
    framework_dir_path: str
    ignore_certificate_errors: bool
    javascript_flags: str
    locale: str
    locales_dir_path: str
    debug: bool
    log_file: str
    log_severity: int
    multi_threaded_message_loop: bool
    net_security_expiration_enabled: bool
    pack_loading_disabled: bool
    persist_session_cookies: bool
    persist_user_preferences: bool
    product_version: str
    remote_debugging_port: int
    resources_dir_path: str
    single_process: bool
    string_encoding: str
    uncaught_exception_stack_size: int
    unique_request_context_per_browser: bool
    user_agent: str
    user_data_path: str
    windowless_rendering_enabled: bool

class BrowserSettings(TypedDict):
    accept_language_list: str
    application_cache_disabled: bool
    background_color: int
    cursive_font_family: str
    databases_disabled: bool
    default_encoding: str
    default_fixed_font_size: int
    default_font_size: int
    dom_paste_disabled: bool
    fantasy_font_family: str
    file_access_from_file_urls_allowed: bool
    fixed_font_family: str
    inherit_client_handlers_for_popups: bool
    image_load_disabled: bool
    javascript_disabled: bool
    javascript_close_windows_disallowed: bool
    javascript_access_clipboard_disallowed: bool
    local_storage_disabled: bool
    minimum_font_size: int
    minimum_logical_font_size: int
    plugins_disabled: bool
    remote_fonts: bool
    sans_serif_font_family: str
    serif_font_family: str
    shrink_standalone_images_to_fit: bool
    standard_font_family: bool
    tab_to_links_disabled: bool
    text_area_resize_disabled: bool
    universal_access_from_file_urls_allowed: bool
    user_style_sheet_location: bool
    web_security_disabled: bool
    webgl_disabled: bool
    windowless_frame_rate: bool

class Browser:
    def AddWordToDictionary(self, word: str) -> None: ...
    def CanGoBack(self) -> bool: ...
    def CanGoForward(self) -> bool: ...
    def CloseBrowser(self, forceClose: bool) -> None: ...
    def CloseDevTools(self) -> bool: ...
    def DragTargetDragEnter(self, x: int, y: int, allowed_ops: int) -> None: ...
    def DragTargetDragOver(self, x: int, y: int, allowed_ops: int) -> None: ...
    def DragTargetDragLeave(self) -> None: ...
    def DragTargetDrop(self, x: int, y: int) -> None: ...
    def DragSourceEndedAt(self, x: int, y: int, operation: int) -> None: ...
    def DragSourceSystemDragEnded(self) -> None: ...
    def ExecuteFunction(self, funcName: str, *params: _JSValue) -> None: ...
    def ExecuteJavascript(self, jsCode: str, scriptUrl: str = "", startLine: int = 1) -> None: ...
    def Find(self, searchId: int, searchText: str, forward: bool, matchCase: bool, findNext: bool) -> None: ...
    def GetClientCallback(self, name: str) -> Callable[..., _JSValue]: ...
    def GetClientCallbacksDict(self) -> dict[str, Callable[..., _JSValue]]: ...
    def GetFocusedFrame(self) -> Frame: ...
    def GetFrame(self, name: str) -> Frame: ...
    def GetFrameByIdentifier(self, identifier: int) -> Frame: ...
    def GetFrames(self) -> list[Frame]: ...
    def GetFrameCount(self) -> int: ...
    # def GetFrameIdentifiers(self) -> None: ...
    def GetFrameNames(self) -> list[str]: ...
    def GetIdentifier(self) -> int: ...
    def GetImage(self) -> _ImageTuple: ...
    def GetJavascriptBindings(self) -> JavascriptBindings: ...
    def GetMainFrame(self) -> Frame: ...
    # def GetNSTextInputContext(self) -> Any: ...
    def GetOpenerWindowHandle(self) -> int | None: ...
    def GetOuterWindowHandle(self) -> int: ...
    def GetSetting(self, key: str) -> _JSValue: ...
    def GetUrl(self) -> str: ...
    def GetUserData(self, key: _JSValue) -> _JSValue: ...
    def GetWindowHandle(self) -> int: ...
    def GetZoomLevel(self) -> float: ...
    def GoBack(self) -> None: ...
    def GoForward(self) -> None: ...
    # def HandleKeyEventAfterTextInputClient(self, keyEvent: Any) -> None: ...
    # def HandleKeyEventBeforeTextInputClient(self) -> None: ...
    def HasDevTools(self) -> bool: ...
    def HasDocument(self) -> bool: ...
    def Invalidate(self, element_type: PaintElementType) -> None: ...
    if sys.platform == "win32":
        def IsFullscreen(self) -> bool: ...
    # def IsLoading(self) -> bool: ...
    def IsMouseCursorChangeDisabled(self) -> bool: ...
    def IsPopup(self) -> bool: ...
    def IsWindowRenderingDisabled(self) -> bool: ...
    def LoadUrl(self, url: str) -> None: ...
    def Navigate(self, url: str) -> None: ...
    def NotifyMoveOrResizeStarted(self) -> None: ...
    def NotifyScreenInfoChanged(self) -> None: ...
    def ParentWindowWillClose(self) -> None: ...
    def Print(self) -> None: ...
    def Reload(self) -> None: ...
    def ReloadIgnoreCache(self) -> None: ...
    def ReplaceMisspelling(self, word: str) -> None: ...
    def SetAutoResizeEnabled(self, enabled: bool, min_size: list[int], max_size: list[int]) -> None: ...
    def SetBounds(self, x: int, y: int, width: int, height: int) -> None: ...
    def SendKeyEvent(self, event: _KeyEvent) -> None: ...
    def SendMouseClickEvent(
        self, x: int, y: int, mouseButtonType: int, mouseUp: bool, clickCount: int, modifiers: KeyEventFlags
    ) -> None: ...
    def SendMouseMoveEvent(self, x: int, y: int, mouseLeave: bool, modifiers: KeyEventFlags) -> None: ...
    def SendMouseWheelEvent(self, x: int, y: int, deltaX: int, deltaY: int, modifiers: KeyEventFlags) -> None: ...
    def SendFocusEvent(self, setFocus: bool) -> None: ...
    def SendCaptureLostEvent(self) -> None: ...
    def SetAccessibilityState(self, state: int) -> None: ...
    def SetClientCallback(self, name: str, callback: Callable[..., _JSValue]) -> None: ...
    def SetClientHandler(self, clientHandler: object) -> None: ...
    def SetFocus(self, focus: bool) -> None: ...
    def SetMouseCursorChangeDisabled(self, disabled: bool) -> None: ...
    def SetJavascriptBindings(self, bindings: JavascriptBindings) -> None: ...
    def SetUserData(self, key: _JSValue, value: _JSValue) -> None: ...
    def SetZoomLevel(self, zoomLevel: float) -> None: ...
    def ShowDevTools(self) -> None: ...
    def StartDownload(self, url: str) -> None: ...
    def StopLoad(self) -> None: ...
    def StopFinding(self, clearSelection: bool) -> None: ...
    def ToggleFullscreen(self) -> bool: ...
    def TryCloseBrowser(self) -> None: ...
    def WasResized(self) -> None: ...
    def WasHidden(self, hidden: bool) -> None: ...

class Callback:
    def Cancel(self) -> None: ...
    def Continue(self) -> None: ...

class Cookie:
    def Set(self, cookie: _Cookie) -> None: ...
    def Get(self) -> _Cookie: ...
    def SetName(self, value: str) -> None: ...
    def GetName(self) -> str: ...
    def SetValue(self, value: str) -> None: ...
    def GetValue(self) -> str: ...
    def SetDomain(self, value: str) -> None: ...
    def GetDomain(self) -> str: ...
    def SetPath(self, value: str) -> None: ...
    def GetPath(self) -> str: ...
    def SetSecure(self, value: bool) -> None: ...
    def GetSecure(self) -> bool: ...
    def SetHttpOnly(self, value: bool) -> None: ...
    def GetHttpOnly(self) -> bool: ...
    def SetCreation(self, value: datetime.datetime) -> None: ...
    def GetCreation(self) -> datetime.datetime: ...
    def SetLastAccess(self, value: datetime.datetime) -> None: ...
    def GetLastAccess(self) -> datetime.datetime: ...
    def SetHasExpires(self, value: bool) -> None: ...
    def GetHasExpires(self) -> bool: ...
    def SetExpires(self, value: datetime.datetime) -> None: ...
    def GetExpires(self) -> datetime.datetime: ...

class CookieManager:
    def GetGlobalManager(self) -> CookieManager: ...
    def GetBlockingManager(self) -> CookieManager: ...
    @staticmethod
    def CreateManager(path: str, persistSessionCookies: bool = False) -> CookieManager: ...
    def SetSupportedSchemes(self, schemes: list[str]) -> None: ...
    def VisitAllCookies(self, object_: CookieVisitor) -> bool: ...
    def VisitUrlCookies(self, url: str, includeHttpOnly: bool, object_: CookieVisitor) -> bool: ...
    def SetCookie(self, url: str, cookie: Cookie) -> None: ...
    def DeleteCookies(self, url: str, cookie_name: str) -> None: ...
    def SetStoragePath(self, path: str, persist_session_cookies: bool = False) -> bool: ...
    def FlushStore(self, _: None = ...) -> bool: ...

if sys.platform == "win32":
    class DpiAware:
        @staticmethod
        def CalculateWindowSize(width: int, height: int) -> tuple[int, int]: ...
        @staticmethod
        def EnableHighDpiSupport() -> None: ...
        @staticmethod
        def GetSystemDpi() -> tuple[int, int]: ...
        @staticmethod
        def IsProcessDpiAware() -> bool: ...
        @staticmethod
        def SetProcessDpiAware() -> None: ...
        @staticmethod
        def Scale(size: int | tuple[int, int] | list[int]) -> tuple[int, int]: ...

class DragData:
    def IsLink(self) -> bool: ...
    def IsFragment(self) -> bool: ...
    def GetLinkUrl(self) -> str: ...
    def GetLinkTitle(self) -> str: ...
    def GetFragmentText(self) -> str: ...
    def GetFragmentHtml(self) -> str: ...
    def GetImage(self) -> Image: ...
    def GetImageHotspot(self) -> Image: ...
    def HasImage(self) -> bool: ...

class Frame:
    def Copy(self) -> None: ...
    def Cut(self) -> None: ...
    def Delete(self) -> None: ...
    def ExecuteFunction(self, funcName: str, *args: _JSValue) -> None: ...
    def ExecuteJavascript(self, jsCode: str, scriptUrl: str = "", startLine: int = 1) -> None: ...
    def GetBrowser(self) -> Browser: ...
    def GetIdentifier(self) -> int: ...
    def GetBrowserIdentifier(self) -> int: ...
    def GetName(self) -> str: ...
    def GetParent(self) -> Frame | None: ...
    def GetSource(self, visitor: StringVisitor) -> None: ...
    def GetText(self, visitor: StringVisitor) -> None: ...
    def GetUrl(self) -> str: ...
    def IsFocused(self) -> bool: ...
    def IsMain(self) -> bool: ...
    def IsValid(self) -> bool: ...
    def LoadString(self, value: str, url: str) -> None: ...
    def LoadUrl(self, url: str) -> None: ...
    def Paste(self) -> None: ...
    def Redo(self) -> None: ...
    def SelectAll(self) -> None: ...
    def Undo(self) -> None: ...
    def ViewSource(self) -> None: ...

class Image:
    def GetAsBitmap(self, scale_factor: float, color_type: int, alpha_type: int) -> bytes: ...
    def GetAsPng(self, scale_factor: float, with_transparency: bool) -> bytes: ...
    def GetHeight(self) -> int: ...
    def GetWidth(self) -> int: ...

class JavascriptBindings:
    def __init__(self, bindToFrames: bool = False, bindToPopups: bool = False) -> None: ...
    def IsValueAllowed(self, value: _JSValue) -> None: ...
    def Rebind(self) -> None: ...
    def SetFunction(self, name: str, func: Callable[..., _JSValue]) -> None: ...
    def SetObject(self, name: str, object_: object) -> None: ...
    def SetProperty(self, name: str, value: _JSValue) -> None: ...

class JavascriptCallback:
    def Call(self, *params: _JSValue) -> None: ...
    def GetFrame(self) -> Frame | None: ...
    def GetId(self) -> int: ...
    def GetFunctionName(self) -> str: ...

class PaintBuffer:
    def GetIntPointer(self) -> int: ...
    def GetBytes(
        self, mode: Literal["bgra", "rgba"] = "bgra", origin: Literal["top-left", "bottom-left"] = "top-left"
    ) -> bytes: ...

class Request:
    @staticmethod
    def CreateRequest() -> Request: ...
    def IsReadOnly(self) -> bool: ...
    def GetUrl(self) -> str: ...
    def SetUrl(self, url: str) -> None: ...
    def GetMethod(self) -> str: ...
    def SetMethod(self, method: str) -> None: ...
    def GetPostData(self) -> list[bytes] | dict[bytes, bytes]: ...
    def SetPostData(self, postData: list[bytes] | dict[bytes, bytes]) -> None: ...
    def GetHeaderMap(self) -> dict[str, str]: ...
    def GetHeaderMultimap(self) -> list[tuple[str, str]]: ...
    def SetHeaderMap(self, headerMap: dict[str, str]) -> None: ...
    def SetHeaderMultimap(self, headerMultimap: list[tuple[str, str]]) -> None: ...
    def GetFlags(self) -> int: ...
    def SetFlags(self, flags: int) -> None: ...
    def GetFirstPartyForCookies(self) -> str: ...
    def SetFirstPartyForCookies(self, url: str) -> None: ...
    def GetResourceType(self) -> int: ...
    # def GetTransitionType(self) -> int: ...

class Response:
    def IsReadOnly(self) -> bool: ...
    def GetStatus(self) -> int: ...
    def SetStatus(self, status: int) -> None: ...
    def GetStatusText(self) -> str: ...
    def SetStatusText(self, statusText: str) -> None: ...
    def GetMimeType(self) -> str: ...
    def SetMimeType(self, mimeType: str) -> None: ...
    def GetHeader(self, name: str) -> str: ...
    def GetHeaderMap(self) -> dict[str, str]: ...
    def GetHeaderMultimap(self) -> list[tuple[str, str]]: ...
    def SetHeaderMap(self, headerMap: dict[str, str]) -> None: ...
    def SetHeaderMultimap(self, headerMultimap: list[tuple[str, str]]) -> None: ...

class WebPluginInfo:
    def GetName(self) -> str: ...
    def GetPath(self) -> str: ...
    def GetVersion(self) -> str: ...
    def GetDescription(self) -> str: ...

class WebRequest:
    @staticmethod
    def Create(request: Request, handler: WebRequestClient) -> WebRequest: ...
    def GetRequest(self) -> Request: ...
    def GetRequestStatus(self) -> Literal["Unknown", "Success", "Pending", "Canceled", "Failed"]: ...
    def GetRequestError(self) -> NetworkError: ...
    def GetResponse(self) -> Response: ...
    def Cancel(self) -> None: ...

class WindowInfo:
    def SetAsChild(self, parentWindowHandle: int, windowRect: tuple[int, int, int, int] | None = ...) -> None: ...
    def SetAsPopup(self, parentWindowHandle: int, windowName: str) -> None: ...
    def SetAsOffscreen(self, parentWindowHandle: int) -> None: ...

class WindowUtils:
    if sys.platform == "win32":
        @staticmethod
        def OnSetFocus(windowHandle: int, msg: int, wparam: int, lparam: int) -> None: ...
        @staticmethod
        def OnSize(windowHandle: int, msg: int, wparam: int, lparam: int) -> None: ...
        @staticmethod
        def OnEraseBackground(windowHandle: int, msg: int, wparam: int, lparam: int) -> None: ...
        @staticmethod
        def SetTitle(browser: Browser, title: str) -> None: ...
        @staticmethod
        def SetIcon(browser: Browser, icon: Literal["inherit"] = "inherit") -> None: ...

    @staticmethod
    def GetParentHandle(windowHandle: int) -> None: ...
    @staticmethod
    def IsWindowHandle(windowHandle: int) -> None: ...

    if sys.platform == "linux":
        @staticmethod
        def gtk_plug_new(GdkNativeWindow: int) -> None: ...
        @staticmethod
        def gtk_widget_show(GtkWidget: int) -> None: ...
        @staticmethod
        def InstallX11ErrorHandlers() -> None: ...

class AccessibilityHandler(Protocol):
    def _OnAccessibilityTreeChange(self, value: list[Any]) -> None: ...
    def _OnAccessibilityLocationChange(self, value: list[Any]) -> None: ...

class DisplayHandler(Protocol):
    def OnAddressChange(self, browser: Browser, frame: Frame, url: str) -> None: ...
    def OnAutoResize(self, browser: Browser, new_size: tuple[int, int]) -> bool: ...
    def OnConsoleMessage(self, browser: Browser, level: int, message: str, source: str, line: int) -> bool: ...
    def OnLoadingProgressChange(self, browser: Browser, progress: float) -> None: ...
    def OnStatusMessage(self, browser: Browser, value: str) -> None: ...
    def OnTitleChange(self, browser: Browser, title: str) -> None: ...
    def OnTooltip(self, browser: Browser, text_out: list[str]) -> bool: ...

class FocusHandler(Protocol):
    def OnTakeFocus(self, browser: Browser, next_component: bool) -> None: ...
    def OnSetFocus(self, browser: Browser, source: int) -> bool: ...
    def OnGotFocus(self, browser: Browser) -> None: ...

class JavascriptDialogCallback(Protocol):
    def Continue(self, allow: bool, user_input: str) -> None: ...

class JavascriptDialogHandler(Protocol):
    def OnJavascriptDialog(
        self,
        origin_url: str,
        dialog_type: int,
        message_text: str,
        default_prompt_text: str,
        callback: JavascriptDialogCallback,
        suppress_message_out: list[Any],
    ) -> bool: ...
    def OnBeforeUnloadJavascriptDialog(
        self, browser: Browser, message_text: str, is_reload: bool, callback: JavascriptDialogCallback
    ) -> bool: ...
    def OnResetJavascriptDialogState(self, browser: Browser) -> None: ...
    def OnJavascriptDialogClosed(self, browser: Browser) -> None: ...

class KeyboardHandler(Protocol):
    def OnPreKeyEvent(
        self, browser: Browser, event: _KeyEvent, event_handle: Any, is_keyboard_shortcut_out: list[Any]
    ) -> bool: ...
    def OnKeyEvent(self, browser: Browser, event: _KeyEvent, event_handle: Any) -> bool: ...

class LifespanHandler(Protocol):
    def DoClose(self, browser: Browser) -> bool: ...
    def _OnAfterCreated(self, browser: Browser) -> None: ...
    def OnBeforeClose(self, browser: Browser) -> None: ...
    def OnBeforePopup(
        self,
        browser: Browser,
        frame: Frame,
        target_url: str,
        target_frame_name: str,
        target_disposition: WindowOpenDisposition,
        user_gesture: bool,
        popup_features: None,
        window_info_out: list[WindowInfo],
        client: None,
        browser_settings_out: list[BrowserSettings],
        no_javascript_access_out: list[bool],
    ) -> bool: ...

class LoadHandler(Protocol):
    def OnLoadingStateChange(self, browser: Browser, is_loading: bool, can_go_back: bool, can_go_forward: bool) -> None: ...
    def OnLoadStart(self, browser: Browser, frame: Frame) -> None: ...
    def OnDomReady(self) -> None: ...
    def OnLoadEnd(self, browser: Browser, frame: Frame, http_code: int) -> None: ...
    def OnLoadError(
        self, browser: Browser, frame: Frame, error_code: NetworkError, error_text_out: list[str], failed_url: str
    ) -> None: ...

class RenderHandler(Protocol):
    def GetRootScreenRect(self, browser: Browser, rect_out: list[int]) -> bool: ...
    def GetViewRect(self, browser: Browser, rect_out: list[int]) -> bool: ...
    def GetScreenRect(self, browser: Browser, rect_out: list[int]) -> bool: ...
    def GetScreenPoint(self, view_x: int, view_y: int, screen_coordinates_out: list[int]) -> bool: ...
    def OnPopupShow(self, browser: Browser, show: bool) -> None: ...
    def OnPopupSize(self, browser: Browser, rect_out: list[int]) -> None: ...
    def OnPaint(
        self,
        browser: Browser,
        element_type: PaintElementType,
        dirty_rects: list[list[int]],
        paint_buffer: PaintBuffer,
        width: int,
        height: int,
    ) -> None: ...
    def OnCursorChange(self, browser: Browser, cursor: int) -> None: ...
    def OnScrollOffsetChanged(self, browser: Browser) -> None: ...
    def OnTextSelectionChanged(self, browser: Browser, selected_text: str, selected_range: list[int]) -> None: ...
    def StartDragging(self, browser: Browser, drag_data: DragData, allowed_ops: int, x: int, y: int) -> None: ...
    def UpdateDragCursor(self, browser: Browser, operation: int) -> None: ...

class AuthCallback(Protocol):
    def Continue(self, username: str, password: str) -> None: ...
    def Cancel(self) -> None: ...

class RequestCallback(Protocol):
    def Continue(self, allow: bool) -> None: ...
    def Cancel(self) -> None: ...

class RequestHandler(Protocol):
    def CanGetCookies(self, browser: Browser, frame: Frame, request: Request) -> bool: ...
    def CanSetCookie(self, browser: Browser, frame: Frame, request: Request, cookie: Cookie) -> bool: ...
    def GetAuthCredentials(
        self,
        browser: Browser,
        frame: Frame,
        is_proxy: bool,
        host: str,
        port: int,
        realm: str,
        scheme: str,
        callback: AuthCallback,
    ) -> bool: ...
    def GetCookieManager(self, browser: Browser | None, main_url: str) -> CookieManager: ...
    def GetResourceHandler(self, browser: Browser, frame: Frame, request: Request) -> ResourceHandler: ...
    def OnBeforeBrowse(self, browser: Browser, frame: Frame, request: Request, user_gesture: bool, is_redirect: bool) -> bool: ...
    def _OnBeforePluginLoad(
        self,
        browser: Browser,
        mime_type: str,
        plugin_url: str,
        is_main_frame: bool,
        top_origin_url: str,
        plugin_info: WebPluginInfo,
    ) -> bool: ...
    def OnBeforeResourceLoad(self, browser: Browser, frame: Frame, request: Request) -> bool: ...
    def _OnCertificateError(self, cert_error: NetworkError, request_url: str, callback: RequestCallback) -> None: ...
    def OnQuotaRequest(self, browser: Browser, origin_url: str, new_size: int, callback: RequestCallback) -> bool: ...
    def OnResourceRedirect(
        self, browser: Browser, frame: Frame, old_url: str, new_url_out: list[str], request: Request, response: Response
    ) -> None: ...
    def OnResourceResponse(self) -> None: ...
    def OnPluginCrashed(self, browser: Browser, plugin_path: str) -> None: ...
    def OnProtocolExecution(self, browser: Browser, url: str, allow_execution_out: list[bool]) -> None: ...
    def OnRendererProcessTerminated(self, browser: Browser, status: TerminationStatus) -> None: ...

class ResourceHandler(Protocol):
    def ProcessRequest(self, request: Request, callback: Callback) -> bool: ...
    def GetResponseHeaders(self, response: Response, response_length_out: list[int], redirect_url_out: list[str]) -> None: ...
    def ReadResponse(self, data_out: list[bytes], bytes_to_read: int, bytes_read_out: list[int], callback: Callback) -> None: ...
    def CanGetCookie(self, cookie: Cookie) -> bool: ...
    def CanSetCookie(self, cookie: Cookie) -> bool: ...
    def Cancel(self) -> None: ...

class V8ContextHandler(Protocol):
    def OnContextCreated(self, browser: Browser, frame: Frame) -> None: ...
    def OnContextReleased(self, browser: Browser, frame: Frame) -> None: ...

class CookieVisitor(Protocol):
    def Visit(self, cookie: Cookie, count: int, total: int, delete_cookie_out: list[bool]) -> bool: ...

class StringVisitor(Protocol):
    def Visit(self, value: str) -> bool: ...

class WebRequestClient(Protocol):
    def OnUploadProgress(self, web_request: WebRequest, current: int, total: int) -> None: ...
    def OnDownloadProgress(self, web_request: WebRequest, current: int, total: int) -> None: ...
    def OnDownloadData(self, web_request: WebRequest, data: bytes) -> None: ...
    def OnRequestComplete(self, web_request: WebRequest) -> None: ...

_JSValue: TypeAlias = (
    bool
    | bytes
    | float
    | int
    | str
    | Callable[..., _JSValue]
    | list[_JSValue]
    | tuple[_JSValue, ...]
    | dict[_JSValue, _JSValue]
    | None
)

class _ImageTuple(NamedTuple):
    buffer: bytes
    width: int
    height: int

class _Cookie(TypedDict, total=False):
    name: str
    value: str
    domain: str
    path: str
    secure: bool
    httpOnly: bool
    creation: datetime.datetime
    lastAccess: datetime.datetime
    hasExpires: bool
    expires: datetime.datetime

class _ContextMenuOptions(TypedDict):
    enabled: bool
    navigation: bool
    print: bool
    view_source: bool
    external_browser: bool
    devtools: bool

class _KeyEvent(TypedDict):
    type: KeyEventType
    modifiers: KeyEventFlags
    windows_key_code: int
    native_key_code: int
    is_system_key: bool
    character: int
    unmodified_character: int
    focus_on_editable_field: bool

class _Version(TypedDict):
    version: str
    chrome_version: str
    cef_version: str
    cef_api_hash_platform: str
    cef_api_hash_universal: str
    cef_commit_hash: str
    cef_commit_number: int

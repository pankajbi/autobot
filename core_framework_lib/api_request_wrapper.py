from requests import request
import logging

logger = logging.getLogger(__name__)


class RunRestRequest(object):

    def __init__(self):
        pass

    @classmethod
    def run_request(cls, method, url, json=None, params=None, headers=None, data=None, files=None,
                    auth=None, timeout=None, allow_redirects=True, proxies=None, stream=None, verify=None, cert=None,
                    cookies=None):
        """
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``,
                ``PATCH``, or ``DELETE``.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read
            timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
                the server's TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to ``True``.
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
            """
        
        response = request(method, url, params=None, data=None, headers=None, cookies=None, files=None,
                           auth=None, timeout=None, allow_redirects=True, proxies=None,
                           hooks=None, stream=None, verify=None, cert=None, json=None)

        return response

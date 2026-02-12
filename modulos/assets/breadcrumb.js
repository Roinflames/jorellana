(function () {
  function prettyName(pathname) {
    var file = pathname.split("/").pop() || "";
    file = decodeURIComponent(file);
    if (!file || file === "index.html") return "Inicio";
    return file.replace(/\.html$/i, "");
  }

  function sameOriginReferrerPath() {
    try {
      if (!document.referrer) return "";
      var ref = new URL(document.referrer);
      if (ref.origin !== window.location.origin) return "";
      return ref.pathname;
    } catch (e) {
      return "";
    }
  }

  function ensureBreadcrumb() {
    var host = document.body;
    if (!host) return;

    var bar = document.createElement("div");
    bar.id = "bcp-breadcrumb";
    bar.style.cssText =
      "position:sticky;top:0;z-index:9998;background:#ffffff;border-bottom:1px solid #e5e7eb;" +
      "padding:10px 14px;font:600 13px/1.4 'Segoe UI',Tahoma,sans-serif;color:#374151;" +
      "display:flex;align-items:center;gap:8px;flex-wrap:wrap";

    var homeLink = document.createElement("a");
    homeLink.href = "/Dashboard%20Principal.html";
    homeLink.textContent = "Dashboard";
    homeLink.style.cssText = "color:#1f4f8a;text-decoration:none";
    bar.appendChild(homeLink);

    var refPath = sameOriginReferrerPath();
    if (refPath && refPath !== window.location.pathname) {
      var sep1 = document.createElement("span");
      sep1.textContent = ">";
      sep1.style.color = "#9ca3af";
      bar.appendChild(sep1);

      var prev = document.createElement("a");
      prev.href = refPath + window.location.search;
      prev.textContent = prettyName(refPath);
      prev.style.cssText = "color:#1f4f8a;text-decoration:none";
      bar.appendChild(prev);
    }

    var sep2 = document.createElement("span");
    sep2.textContent = ">";
    sep2.style.color = "#9ca3af";
    bar.appendChild(sep2);

    var current = document.createElement("span");
    current.textContent = prettyName(window.location.pathname);
    current.style.color = "#111827";
    bar.appendChild(current);

    var backBtn = document.createElement("button");
    backBtn.type = "button";
    backBtn.textContent = "Atras";
    backBtn.style.cssText =
      "margin-left:auto;background:#f3f4f6;border:1px solid #d1d5db;border-radius:8px;" +
      "padding:4px 10px;color:#111827;cursor:pointer";
    backBtn.onclick = function () {
      if (window.history.length > 1) {
        window.history.back();
      } else {
        window.location.href = "/Dashboard%20Principal.html";
      }
    };
    bar.appendChild(backBtn);

    document.body.insertBefore(bar, document.body.firstChild);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", ensureBreadcrumb);
  } else {
    ensureBreadcrumb();
  }
})();

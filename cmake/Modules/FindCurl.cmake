find_path(CURL_INCLUDE_DIR curl.h)

find_library(CURL_LIBRARY NAMES libcurl)
#find_library(CHARSET_LIBRARY NAMES charset libcharset)

if (CURL_INCLUDE_DIR AND CURL_LIBRARY)
    set(CURL_FOUND TRUE)
endif (CURL_INCLUDE_DIR AND CURL_LIBRARY)

mark_as_advanced(
        CURL_INCLUDE_DIR
        CURL_LIBRARY
        CHARSET_LIBRARY
)

if (CURL_FOUND)
    set(CURL_INCLUDE_DIRS ${CURL_INCLUDE_DIR})
    set(CURL_LIBRARIES ${CURL_LIBRARY})
    set(CURL_AND_DEPS_LIBRARIES ${CURL_LIBRARY} ${CHARSET_LIBRARY})
    message(STATUS "Found Iconv and it's dependencies: ${CURL_AND_DEPS_LIBRARIES}")
else (CURL_FOUND)
    message(FATAL_ERROR "Could not find curl")
endif (CURL_FOUND)

find_path(ICONV_INCLUDE_DIR iconv.h)

find_library(ICONV_LIBRARY NAMES iconv libiconv libiconv-2 c)
find_library(CHARSET_LIBRARY NAMES charset libcharset)

if (ICONV_INCLUDE_DIR AND ICONV_LIBRARY)
    set(ICONV_FOUND TRUE)
endif (ICONV_INCLUDE_DIR AND ICONV_LIBRARY)

mark_as_advanced(
        ICONV_INCLUDE_DIR
        ICONV_LIBRARY
        CHARSET_LIBRARY
)

if (ICONV_FOUND)
    set(ICONV_INCLUDE_DIRS ${ICONV_INCLUDE_DIR})
    set(ICONV_LIBRARIES ${ICONV_LIBRARY})
    set(ICONV_AND_DEPS_LIBRARIES ${ICONV_LIBRARY} ${CHARSET_LIBRARY})
    message(STATUS "Found Iconv and it's dependencies: ${ICONV_AND_DEPS_LIBRARIES}")
else (ICONV_FOUND)
    message(FATAL_ERROR "Could not find Iconv")
endif (ICONV_FOUND)

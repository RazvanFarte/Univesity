%ifndef _MSDN_DEFS_INC_
%define _MSDN_DEFS_INC_

%define NULL            0
%define MAX_PATH        260

%define GENERIC_READ                        0x80000000
%define GENERIC_WRITE                       0x40000000
%define GENERIC_EXECUTE                     0x20000000
%define GENERIC_ALL                         0x10000000

%define FILE_SHARE_READ                     0x00000001  
%define FILE_SHARE_WRITE                    0x00000002  
%define FILE_SHARE_DELETE                   0x00000004  

%define FILE_ATTRIBUTE_READONLY             0x00000001  
%define FILE_ATTRIBUTE_HIDDEN               0x00000002  
%define FILE_ATTRIBUTE_SYSTEM               0x00000004  
%define FILE_ATTRIBUTE_DIRECTORY            0x00000010  
%define FILE_ATTRIBUTE_ARCHIVE              0x00000020  
%define FILE_ATTRIBUTE_DEVICE               0x00000040  
%define FILE_ATTRIBUTE_NORMAL               0x00000080  
%define FILE_ATTRIBUTE_TEMPORARY            0x00000100  
%define FILE_ATTRIBUTE_SPARSE_FILE          0x00000200  
%define FILE_ATTRIBUTE_REPARSE_POINT        0x00000400  
%define FILE_ATTRIBUTE_COMPRESSED           0x00000800  
%define FILE_ATTRIBUTE_OFFLINE              0x00001000  
%define FILE_ATTRIBUTE_NOT_CONTENT_INDEXED  0x00002000  
%define FILE_ATTRIBUTE_ENCRYPTED            0x00004000  
%define FILE_ATTRIBUTE_INTEGRITY_STREAM     0x00008000  
%define FILE_ATTRIBUTE_VIRTUAL              0x00010000  
%define FILE_ATTRIBUTE_NO_SCRUB_DATA        0x00020000  
%define FILE_ATTRIBUTE_EA                   0x00040000  

%define CREATE_NEW                          1
%define CREATE_ALWAYS                       2
%define OPEN_EXISTING                       3
%define OPEN_ALWAYS                         4
%define TRUNCATE_EXISTING                   5

%define INVALID_HANDLE_VALUE                0xFFFFFFFF
%define INVALID_FILE_SIZE                   0xFFFFFFFF
%define INVALID_SET_FILE_POINTER            0xFFFFFFFF
%define INVALID_FILE_ATTRIBUTES             0xFFFFFFFF

%define FILE_BEGIN                          0
%define FILE_CURRENT                        1
%define FILE_END                            2

%define ERROR_FILE_NOT_FOUND                0x2
%define ERROR_NO_MORE_FILES                 0x12

%define CreateFileA                         _CreateFileA@28
%define ReadFile                            _ReadFile@20
%define WriteFile                           _WriteFile@20
%define SetFilePointer                      _SetFilePointer@16
%define CloseHandle                         _CloseHandle@4
%define GetLastError                        _GetLastError@0
%define FindFirstFileA                      _FindFirstFileA@8
%define FindNextFileA                       _FindNextFileA@8
%define FindClose                           _FindClose@4
%define GetFileSize                         _GetFileSize@8
%define GetFileAttributesA                  _GetFileAttributesA@4
%define CancelIo							_CancelIo@4

%define CreateFile                          CreateFileA
%define FindFirstFile                       FindFirstFileA
%define FindNextFile                        FindNextFileA
%define GetFileAttributes 					GetFileAttributesA

%define GetComputerNameA					_GetComputerNameA@8
%define GetComputerName						GetComputerNameA

%define CreateFile							CreateFileA

struc FILETIME
.dwLowDateTime resd 1
.dwHighDateTime resd 1
endstruc

struc WIN32_FIND_DATA
.dwFileAttributes 	resd 1
.ftCreationTime	  	resb FILETIME_size
.ftLastAccessTime	resb FILETIME_size
.ftLastWriteTime	resb FILETIME_size
.nFileSizeHigh 		resd 1
.nFileSizeLow		resd 1
.dwReserved0		resd 1
.dwReserved1		resd 1
.cFileName 			resb 260
.cAlternateFileName resb 14
endstruc

struc Student
.nume:				resb 20
.prenume:			resb 20
.varsta:			resb 1
.inaltime:			resb 1
.ochi:				resb 15
endstruc

%endif  ; !_MSDN_DEFS_INC_
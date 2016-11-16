# File generated by tools/make_ssl_data.py
# Generated on 2016-11-10T17:38:59.402032

from _openssl import ffi, lib 
_lib_codes = []
_lib_codes.append(("PEM", lib.ERR_LIB_PEM))
_lib_codes.append(("SSL", lib.ERR_LIB_SSL))
_lib_codes.append(("X509", lib.ERR_LIB_X509))
_error_codes = []
_error_codes.append(("BAD_BASE64_DECODE", lib.ERR_LIB_PEM, 100))
_error_codes.append(("BAD_DECRYPT", lib.ERR_LIB_PEM, 101))
_error_codes.append(("BAD_END_LINE", lib.ERR_LIB_PEM, 102))
_error_codes.append(("BAD_IV_CHARS", lib.ERR_LIB_PEM, 103))
_error_codes.append(("BAD_MAGIC_NUMBER", lib.ERR_LIB_PEM, 116))
_error_codes.append(("BAD_PASSWORD_READ", lib.ERR_LIB_PEM, 104))
_error_codes.append(("BAD_VERSION_NUMBER", lib.ERR_LIB_PEM, 117))
_error_codes.append(("BIO_WRITE_FAILURE", lib.ERR_LIB_PEM, 118))
_error_codes.append(("CIPHER_IS_NULL", lib.ERR_LIB_PEM, 127))
_error_codes.append(("ERROR_CONVERTING_PRIVATE_KEY", lib.ERR_LIB_PEM, 115))
_error_codes.append(("EXPECTING_PRIVATE_KEY_BLOB", lib.ERR_LIB_PEM, 119))
_error_codes.append(("EXPECTING_PUBLIC_KEY_BLOB", lib.ERR_LIB_PEM, 120))
_error_codes.append(("INCONSISTENT_HEADER", lib.ERR_LIB_PEM, 121))
_error_codes.append(("KEYBLOB_HEADER_PARSE_ERROR", lib.ERR_LIB_PEM, 122))
_error_codes.append(("KEYBLOB_TOO_SHORT", lib.ERR_LIB_PEM, 123))
_error_codes.append(("NOT_DEK_INFO", lib.ERR_LIB_PEM, 105))
_error_codes.append(("NOT_ENCRYPTED", lib.ERR_LIB_PEM, 106))
_error_codes.append(("NOT_PROC_TYPE", lib.ERR_LIB_PEM, 107))
_error_codes.append(("NO_START_LINE", lib.ERR_LIB_PEM, 108))
_error_codes.append(("PROBLEMS_GETTING_PASSWORD", lib.ERR_LIB_PEM, 109))
_error_codes.append(("PUBLIC_KEY_NO_RSA", lib.ERR_LIB_PEM, 110))
_error_codes.append(("PVK_DATA_TOO_SHORT", lib.ERR_LIB_PEM, 124))
_error_codes.append(("PVK_TOO_SHORT", lib.ERR_LIB_PEM, 125))
_error_codes.append(("READ_KEY", lib.ERR_LIB_PEM, 111))
_error_codes.append(("SHORT_HEADER", lib.ERR_LIB_PEM, 112))
_error_codes.append(("UNSUPPORTED_ENCRYPTION", lib.ERR_LIB_PEM, 114))
_error_codes.append(("UNSUPPORTED_KEY_COMPONENTS", lib.ERR_LIB_PEM, 126))
_error_codes.append(("APP_DATA_IN_HANDSHAKE", lib.ERR_LIB_SSL, 100))
_error_codes.append(("ATTEMPT_TO_REUSE_SESSION_IN_DIFFERENT_CONTEXT", lib.ERR_LIB_SSL, 272))
_error_codes.append(("BAD_ALERT_RECORD", lib.ERR_LIB_SSL, 101))
_error_codes.append(("BAD_AUTHENTICATION_TYPE", lib.ERR_LIB_SSL, 102))
_error_codes.append(("BAD_CHANGE_CIPHER_SPEC", lib.ERR_LIB_SSL, 103))
_error_codes.append(("BAD_CHECKSUM", lib.ERR_LIB_SSL, 104))
_error_codes.append(("BAD_DATA", lib.ERR_LIB_SSL, 390))
_error_codes.append(("BAD_DATA_RETURNED_BY_CALLBACK", lib.ERR_LIB_SSL, 106))
_error_codes.append(("BAD_DECOMPRESSION", lib.ERR_LIB_SSL, 107))
_error_codes.append(("BAD_DH_G_LENGTH", lib.ERR_LIB_SSL, 108))
_error_codes.append(("BAD_DH_PUB_KEY_LENGTH", lib.ERR_LIB_SSL, 109))
_error_codes.append(("BAD_DH_P_LENGTH", lib.ERR_LIB_SSL, 110))
_error_codes.append(("BAD_DIGEST_LENGTH", lib.ERR_LIB_SSL, 111))
_error_codes.append(("BAD_DSA_SIGNATURE", lib.ERR_LIB_SSL, 112))
_error_codes.append(("BAD_ECC_CERT", lib.ERR_LIB_SSL, 304))
_error_codes.append(("BAD_ECDSA_SIGNATURE", lib.ERR_LIB_SSL, 305))
_error_codes.append(("BAD_ECPOINT", lib.ERR_LIB_SSL, 306))
_error_codes.append(("BAD_HANDSHAKE_LENGTH", lib.ERR_LIB_SSL, 332))
_error_codes.append(("BAD_HELLO_REQUEST", lib.ERR_LIB_SSL, 105))
_error_codes.append(("BAD_LENGTH", lib.ERR_LIB_SSL, 271))
_error_codes.append(("BAD_MAC_DECODE", lib.ERR_LIB_SSL, 113))
_error_codes.append(("BAD_MAC_LENGTH", lib.ERR_LIB_SSL, 333))
_error_codes.append(("BAD_MESSAGE_TYPE", lib.ERR_LIB_SSL, 114))
_error_codes.append(("BAD_PACKET_LENGTH", lib.ERR_LIB_SSL, 115))
_error_codes.append(("BAD_PROTOCOL_VERSION_NUMBER", lib.ERR_LIB_SSL, 116))
_error_codes.append(("BAD_PSK_IDENTITY_HINT_LENGTH", lib.ERR_LIB_SSL, 316))
_error_codes.append(("BAD_RESPONSE_ARGUMENT", lib.ERR_LIB_SSL, 117))
_error_codes.append(("BAD_RSA_DECRYPT", lib.ERR_LIB_SSL, 118))
_error_codes.append(("BAD_RSA_ENCRYPT", lib.ERR_LIB_SSL, 119))
_error_codes.append(("BAD_RSA_E_LENGTH", lib.ERR_LIB_SSL, 120))
_error_codes.append(("BAD_RSA_MODULUS_LENGTH", lib.ERR_LIB_SSL, 121))
_error_codes.append(("BAD_RSA_SIGNATURE", lib.ERR_LIB_SSL, 122))
_error_codes.append(("BAD_SIGNATURE", lib.ERR_LIB_SSL, 123))
_error_codes.append(("BAD_SRP_A_LENGTH", lib.ERR_LIB_SSL, 347))
_error_codes.append(("BAD_SRP_B_LENGTH", lib.ERR_LIB_SSL, 348))
_error_codes.append(("BAD_SRP_G_LENGTH", lib.ERR_LIB_SSL, 349))
_error_codes.append(("BAD_SRP_N_LENGTH", lib.ERR_LIB_SSL, 350))
_error_codes.append(("BAD_SRP_PARAMETERS", lib.ERR_LIB_SSL, 371))
_error_codes.append(("BAD_SRP_S_LENGTH", lib.ERR_LIB_SSL, 351))
_error_codes.append(("BAD_SRTP_MKI_VALUE", lib.ERR_LIB_SSL, 352))
_error_codes.append(("BAD_SRTP_PROTECTION_PROFILE_LIST", lib.ERR_LIB_SSL, 353))
_error_codes.append(("BAD_SSL_FILETYPE", lib.ERR_LIB_SSL, 124))
_error_codes.append(("BAD_SSL_SESSION_ID_LENGTH", lib.ERR_LIB_SSL, 125))
_error_codes.append(("BAD_STATE", lib.ERR_LIB_SSL, 126))
_error_codes.append(("BAD_VALUE", lib.ERR_LIB_SSL, 384))
_error_codes.append(("BAD_WRITE_RETRY", lib.ERR_LIB_SSL, 127))
_error_codes.append(("BIO_NOT_SET", lib.ERR_LIB_SSL, 128))
_error_codes.append(("BLOCK_CIPHER_PAD_IS_WRONG", lib.ERR_LIB_SSL, 129))
_error_codes.append(("BN_LIB", lib.ERR_LIB_SSL, 130))
_error_codes.append(("CA_DN_LENGTH_MISMATCH", lib.ERR_LIB_SSL, 131))
_error_codes.append(("CA_DN_TOO_LONG", lib.ERR_LIB_SSL, 132))
_error_codes.append(("CA_KEY_TOO_SMALL", lib.ERR_LIB_SSL, 397))
_error_codes.append(("CA_MD_TOO_WEAK", lib.ERR_LIB_SSL, 398))
_error_codes.append(("CCS_RECEIVED_EARLY", lib.ERR_LIB_SSL, 133))
_error_codes.append(("CERTIFICATE_VERIFY_FAILED", lib.ERR_LIB_SSL, 134))
_error_codes.append(("CERT_CB_ERROR", lib.ERR_LIB_SSL, 377))
_error_codes.append(("CERT_LENGTH_MISMATCH", lib.ERR_LIB_SSL, 135))
_error_codes.append(("CHALLENGE_IS_DIFFERENT", lib.ERR_LIB_SSL, 136))
_error_codes.append(("CIPHER_CODE_WRONG_LENGTH", lib.ERR_LIB_SSL, 137))
_error_codes.append(("CIPHER_OR_HASH_UNAVAILABLE", lib.ERR_LIB_SSL, 138))
_error_codes.append(("CIPHER_TABLE_SRC_ERROR", lib.ERR_LIB_SSL, 139))
_error_codes.append(("CLIENTHELLO_TLSEXT", lib.ERR_LIB_SSL, 226))
_error_codes.append(("COMPRESSED_LENGTH_TOO_LONG", lib.ERR_LIB_SSL, 140))
_error_codes.append(("COMPRESSION_DISABLED", lib.ERR_LIB_SSL, 343))
_error_codes.append(("COMPRESSION_FAILURE", lib.ERR_LIB_SSL, 141))
_error_codes.append(("COMPRESSION_ID_NOT_WITHIN_PRIVATE_RANGE", lib.ERR_LIB_SSL, 307))
_error_codes.append(("COMPRESSION_LIBRARY_ERROR", lib.ERR_LIB_SSL, 142))
_error_codes.append(("CONNECTION_ID_IS_DIFFERENT", lib.ERR_LIB_SSL, 143))
_error_codes.append(("CONNECTION_TYPE_NOT_SET", lib.ERR_LIB_SSL, 144))
_error_codes.append(("COOKIE_MISMATCH", lib.ERR_LIB_SSL, 308))
_error_codes.append(("DATA_BETWEEN_CCS_AND_FINISHED", lib.ERR_LIB_SSL, 145))
_error_codes.append(("DATA_LENGTH_TOO_LONG", lib.ERR_LIB_SSL, 146))
_error_codes.append(("DECRYPTION_FAILED", lib.ERR_LIB_SSL, 147))
_error_codes.append(("DECRYPTION_FAILED_OR_BAD_RECORD_MAC", lib.ERR_LIB_SSL, 281))
_error_codes.append(("DH_KEY_TOO_SMALL", lib.ERR_LIB_SSL, 372))
_error_codes.append(("DH_PUBLIC_VALUE_LENGTH_IS_WRONG", lib.ERR_LIB_SSL, 148))
_error_codes.append(("DIGEST_CHECK_FAILED", lib.ERR_LIB_SSL, 149))
_error_codes.append(("DTLS_MESSAGE_TOO_BIG", lib.ERR_LIB_SSL, 334))
_error_codes.append(("DUPLICATE_COMPRESSION_ID", lib.ERR_LIB_SSL, 309))
_error_codes.append(("ECC_CERT_NOT_FOR_KEY_AGREEMENT", lib.ERR_LIB_SSL, 317))
_error_codes.append(("ECC_CERT_NOT_FOR_SIGNING", lib.ERR_LIB_SSL, 318))
_error_codes.append(("ECC_CERT_SHOULD_HAVE_RSA_SIGNATURE", lib.ERR_LIB_SSL, 322))
_error_codes.append(("ECC_CERT_SHOULD_HAVE_SHA1_SIGNATURE", lib.ERR_LIB_SSL, 323))
_error_codes.append(("ECDH_REQUIRED_FOR_SUITEB_MODE", lib.ERR_LIB_SSL, 374))
_error_codes.append(("ECGROUP_TOO_LARGE_FOR_CIPHER", lib.ERR_LIB_SSL, 310))
_error_codes.append(("EE_KEY_TOO_SMALL", lib.ERR_LIB_SSL, 399))
_error_codes.append(("EMPTY_SRTP_PROTECTION_PROFILE_LIST", lib.ERR_LIB_SSL, 354))
_error_codes.append(("ENCRYPTED_LENGTH_TOO_LONG", lib.ERR_LIB_SSL, 150))
_error_codes.append(("ERROR_GENERATING_TMP_RSA_KEY", lib.ERR_LIB_SSL, 282))
_error_codes.append(("ERROR_IN_RECEIVED_CIPHER_LIST", lib.ERR_LIB_SSL, 151))
_error_codes.append(("EXCESSIVE_MESSAGE_SIZE", lib.ERR_LIB_SSL, 152))
_error_codes.append(("EXTRA_DATA_IN_MESSAGE", lib.ERR_LIB_SSL, 153))
_error_codes.append(("GOT_A_FIN_BEFORE_A_CCS", lib.ERR_LIB_SSL, 154))
_error_codes.append(("GOT_NEXT_PROTO_BEFORE_A_CCS", lib.ERR_LIB_SSL, 355))
_error_codes.append(("GOT_NEXT_PROTO_WITHOUT_EXTENSION", lib.ERR_LIB_SSL, 356))
_error_codes.append(("HTTPS_PROXY_REQUEST", lib.ERR_LIB_SSL, 155))
_error_codes.append(("HTTP_REQUEST", lib.ERR_LIB_SSL, 156))
_error_codes.append(("ILLEGAL_PADDING", lib.ERR_LIB_SSL, 283))
_error_codes.append(("ILLEGAL_SUITEB_DIGEST", lib.ERR_LIB_SSL, 380))
_error_codes.append(("INAPPROPRIATE_FALLBACK", lib.ERR_LIB_SSL, 373))
_error_codes.append(("INCONSISTENT_COMPRESSION", lib.ERR_LIB_SSL, 340))
_error_codes.append(("INVALID_CHALLENGE_LENGTH", lib.ERR_LIB_SSL, 158))
_error_codes.append(("INVALID_COMMAND", lib.ERR_LIB_SSL, 280))
_error_codes.append(("INVALID_COMPRESSION_ALGORITHM", lib.ERR_LIB_SSL, 341))
_error_codes.append(("INVALID_NULL_CMD_NAME", lib.ERR_LIB_SSL, 385))
_error_codes.append(("INVALID_PURPOSE", lib.ERR_LIB_SSL, 278))
_error_codes.append(("INVALID_SERVERINFO_DATA", lib.ERR_LIB_SSL, 388))
_error_codes.append(("INVALID_SRP_USERNAME", lib.ERR_LIB_SSL, 357))
_error_codes.append(("INVALID_STATUS_RESPONSE", lib.ERR_LIB_SSL, 328))
_error_codes.append(("INVALID_TICKET_KEYS_LENGTH", lib.ERR_LIB_SSL, 325))
_error_codes.append(("KEY_ARG_TOO_LONG", lib.ERR_LIB_SSL, 284))
_error_codes.append(("KRB5", lib.ERR_LIB_SSL, 285))
_error_codes.append(("KRB5_C_CC_PRINC", lib.ERR_LIB_SSL, 286))
_error_codes.append(("KRB5_C_GET_CRED", lib.ERR_LIB_SSL, 287))
_error_codes.append(("KRB5_C_INIT", lib.ERR_LIB_SSL, 288))
_error_codes.append(("KRB5_C_MK_REQ", lib.ERR_LIB_SSL, 289))
_error_codes.append(("KRB5_S_BAD_TICKET", lib.ERR_LIB_SSL, 290))
_error_codes.append(("KRB5_S_INIT", lib.ERR_LIB_SSL, 291))
_error_codes.append(("KRB5_S_RD_REQ", lib.ERR_LIB_SSL, 292))
_error_codes.append(("KRB5_S_TKT_EXPIRED", lib.ERR_LIB_SSL, 293))
_error_codes.append(("KRB5_S_TKT_NYV", lib.ERR_LIB_SSL, 294))
_error_codes.append(("KRB5_S_TKT_SKEW", lib.ERR_LIB_SSL, 295))
_error_codes.append(("LENGTH_MISMATCH", lib.ERR_LIB_SSL, 159))
_error_codes.append(("LENGTH_TOO_SHORT", lib.ERR_LIB_SSL, 160))
_error_codes.append(("LIBRARY_BUG", lib.ERR_LIB_SSL, 274))
_error_codes.append(("LIBRARY_HAS_NO_CIPHERS", lib.ERR_LIB_SSL, 161))
_error_codes.append(("MESSAGE_TOO_LONG", lib.ERR_LIB_SSL, 296))
_error_codes.append(("MISSING_DH_DSA_CERT", lib.ERR_LIB_SSL, 162))
_error_codes.append(("MISSING_DH_KEY", lib.ERR_LIB_SSL, 163))
_error_codes.append(("MISSING_DH_RSA_CERT", lib.ERR_LIB_SSL, 164))
_error_codes.append(("MISSING_DSA_SIGNING_CERT", lib.ERR_LIB_SSL, 165))
_error_codes.append(("MISSING_ECDH_CERT", lib.ERR_LIB_SSL, 382))
_error_codes.append(("MISSING_ECDSA_SIGNING_CERT", lib.ERR_LIB_SSL, 381))
_error_codes.append(("MISSING_EXPORT_TMP_DH_KEY", lib.ERR_LIB_SSL, 166))
_error_codes.append(("MISSING_EXPORT_TMP_RSA_KEY", lib.ERR_LIB_SSL, 167))
_error_codes.append(("MISSING_RSA_CERTIFICATE", lib.ERR_LIB_SSL, 168))
_error_codes.append(("MISSING_RSA_ENCRYPTING_CERT", lib.ERR_LIB_SSL, 169))
_error_codes.append(("MISSING_RSA_SIGNING_CERT", lib.ERR_LIB_SSL, 170))
_error_codes.append(("MISSING_SRP_PARAM", lib.ERR_LIB_SSL, 358))
_error_codes.append(("MISSING_TMP_DH_KEY", lib.ERR_LIB_SSL, 171))
_error_codes.append(("MISSING_TMP_ECDH_KEY", lib.ERR_LIB_SSL, 311))
_error_codes.append(("MISSING_TMP_RSA_KEY", lib.ERR_LIB_SSL, 172))
_error_codes.append(("MISSING_TMP_RSA_PKEY", lib.ERR_LIB_SSL, 173))
_error_codes.append(("MISSING_VERIFY_MESSAGE", lib.ERR_LIB_SSL, 174))
_error_codes.append(("MULTIPLE_SGC_RESTARTS", lib.ERR_LIB_SSL, 346))
_error_codes.append(("NON_SSLV2_INITIAL_PACKET", lib.ERR_LIB_SSL, 175))
_error_codes.append(("NO_CERTIFICATES_RETURNED", lib.ERR_LIB_SSL, 176))
_error_codes.append(("NO_CERTIFICATE_ASSIGNED", lib.ERR_LIB_SSL, 177))
_error_codes.append(("NO_CERTIFICATE_RETURNED", lib.ERR_LIB_SSL, 178))
_error_codes.append(("NO_CERTIFICATE_SET", lib.ERR_LIB_SSL, 179))
_error_codes.append(("NO_CERTIFICATE_SPECIFIED", lib.ERR_LIB_SSL, 180))
_error_codes.append(("NO_CIPHERS_AVAILABLE", lib.ERR_LIB_SSL, 181))
_error_codes.append(("NO_CIPHERS_PASSED", lib.ERR_LIB_SSL, 182))
_error_codes.append(("NO_CIPHERS_SPECIFIED", lib.ERR_LIB_SSL, 183))
_error_codes.append(("NO_CIPHER_LIST", lib.ERR_LIB_SSL, 184))
_error_codes.append(("NO_CIPHER_MATCH", lib.ERR_LIB_SSL, 185))
_error_codes.append(("NO_CLIENT_CERT_METHOD", lib.ERR_LIB_SSL, 331))
_error_codes.append(("NO_CLIENT_CERT_RECEIVED", lib.ERR_LIB_SSL, 186))
_error_codes.append(("NO_COMPRESSION_SPECIFIED", lib.ERR_LIB_SSL, 187))
_error_codes.append(("NO_GOST_CERTIFICATE_SENT_BY_PEER", lib.ERR_LIB_SSL, 330))
_error_codes.append(("NO_METHOD_SPECIFIED", lib.ERR_LIB_SSL, 188))
_error_codes.append(("NO_PEM_EXTENSIONS", lib.ERR_LIB_SSL, 389))
_error_codes.append(("NO_PRIVATEKEY", lib.ERR_LIB_SSL, 189))
_error_codes.append(("NO_PRIVATE_KEY_ASSIGNED", lib.ERR_LIB_SSL, 190))
_error_codes.append(("NO_PROTOCOLS_AVAILABLE", lib.ERR_LIB_SSL, 191))
_error_codes.append(("NO_PUBLICKEY", lib.ERR_LIB_SSL, 192))
_error_codes.append(("NO_RENEGOTIATION", lib.ERR_LIB_SSL, 339))
_error_codes.append(("NO_REQUIRED_DIGEST", lib.ERR_LIB_SSL, 324))
_error_codes.append(("NO_SHARED_CIPHER", lib.ERR_LIB_SSL, 193))
_error_codes.append(("NO_SHARED_SIGATURE_ALGORITHMS", lib.ERR_LIB_SSL, 376))
_error_codes.append(("NO_SRTP_PROFILES", lib.ERR_LIB_SSL, 359))
_error_codes.append(("NO_VERIFY_CALLBACK", lib.ERR_LIB_SSL, 194))
_error_codes.append(("NULL_SSL_CTX", lib.ERR_LIB_SSL, 195))
_error_codes.append(("NULL_SSL_METHOD_PASSED", lib.ERR_LIB_SSL, 196))
_error_codes.append(("OLD_SESSION_CIPHER_NOT_RETURNED", lib.ERR_LIB_SSL, 197))
_error_codes.append(("OLD_SESSION_COMPRESSION_ALGORITHM_NOT_RETURNED", lib.ERR_LIB_SSL, 344))
_error_codes.append(("ONLY_DTLS_1_2_ALLOWED_IN_SUITEB_MODE", lib.ERR_LIB_SSL, 387))
_error_codes.append(("ONLY_TLS_1_2_ALLOWED_IN_SUITEB_MODE", lib.ERR_LIB_SSL, 379))
_error_codes.append(("ONLY_TLS_ALLOWED_IN_FIPS_MODE", lib.ERR_LIB_SSL, 297))
_error_codes.append(("OPAQUE_PRF_INPUT_TOO_LONG", lib.ERR_LIB_SSL, 327))
_error_codes.append(("PACKET_LENGTH_TOO_LONG", lib.ERR_LIB_SSL, 198))
_error_codes.append(("PARSE_TLSEXT", lib.ERR_LIB_SSL, 227))
_error_codes.append(("PATH_TOO_LONG", lib.ERR_LIB_SSL, 270))
_error_codes.append(("PEER_DID_NOT_RETURN_A_CERTIFICATE", lib.ERR_LIB_SSL, 199))
_error_codes.append(("PEER_ERROR", lib.ERR_LIB_SSL, 200))
_error_codes.append(("PEER_ERROR_CERTIFICATE", lib.ERR_LIB_SSL, 201))
_error_codes.append(("PEER_ERROR_NO_CERTIFICATE", lib.ERR_LIB_SSL, 202))
_error_codes.append(("PEER_ERROR_NO_CIPHER", lib.ERR_LIB_SSL, 203))
_error_codes.append(("PEER_ERROR_UNSUPPORTED_CERTIFICATE_TYPE", lib.ERR_LIB_SSL, 204))
_error_codes.append(("PEM_NAME_BAD_PREFIX", lib.ERR_LIB_SSL, 391))
_error_codes.append(("PEM_NAME_TOO_SHORT", lib.ERR_LIB_SSL, 392))
_error_codes.append(("PRE_MAC_LENGTH_TOO_LONG", lib.ERR_LIB_SSL, 205))
_error_codes.append(("PROBLEMS_MAPPING_CIPHER_FUNCTIONS", lib.ERR_LIB_SSL, 206))
_error_codes.append(("PROTOCOL_IS_SHUTDOWN", lib.ERR_LIB_SSL, 207))
_error_codes.append(("PSK_IDENTITY_NOT_FOUND", lib.ERR_LIB_SSL, 223))
_error_codes.append(("PSK_NO_CLIENT_CB", lib.ERR_LIB_SSL, 224))
_error_codes.append(("PSK_NO_SERVER_CB", lib.ERR_LIB_SSL, 225))
_error_codes.append(("PUBLIC_KEY_ENCRYPT_ERROR", lib.ERR_LIB_SSL, 208))
_error_codes.append(("PUBLIC_KEY_IS_NOT_RSA", lib.ERR_LIB_SSL, 209))
_error_codes.append(("PUBLIC_KEY_NOT_RSA", lib.ERR_LIB_SSL, 210))
_error_codes.append(("READ_BIO_NOT_SET", lib.ERR_LIB_SSL, 211))
_error_codes.append(("READ_TIMEOUT_EXPIRED", lib.ERR_LIB_SSL, 312))
_error_codes.append(("READ_WRONG_PACKET_TYPE", lib.ERR_LIB_SSL, 212))
_error_codes.append(("RECORD_LENGTH_MISMATCH", lib.ERR_LIB_SSL, 213))
_error_codes.append(("RECORD_TOO_LARGE", lib.ERR_LIB_SSL, 214))
_error_codes.append(("RECORD_TOO_SMALL", lib.ERR_LIB_SSL, 298))
_error_codes.append(("RENEGOTIATE_EXT_TOO_LONG", lib.ERR_LIB_SSL, 335))
_error_codes.append(("RENEGOTIATION_ENCODING_ERR", lib.ERR_LIB_SSL, 336))
_error_codes.append(("RENEGOTIATION_MISMATCH", lib.ERR_LIB_SSL, 337))
_error_codes.append(("REQUIRED_CIPHER_MISSING", lib.ERR_LIB_SSL, 215))
_error_codes.append(("REQUIRED_COMPRESSSION_ALGORITHM_MISSING", lib.ERR_LIB_SSL, 342))
_error_codes.append(("REUSE_CERT_LENGTH_NOT_ZERO", lib.ERR_LIB_SSL, 216))
_error_codes.append(("REUSE_CERT_TYPE_NOT_ZERO", lib.ERR_LIB_SSL, 217))
_error_codes.append(("REUSE_CIPHER_LIST_NOT_ZERO", lib.ERR_LIB_SSL, 218))
_error_codes.append(("SCSV_RECEIVED_WHEN_RENEGOTIATING", lib.ERR_LIB_SSL, 345))
_error_codes.append(("SERVERHELLO_TLSEXT", lib.ERR_LIB_SSL, 275))
_error_codes.append(("SESSION_ID_CONTEXT_UNINITIALIZED", lib.ERR_LIB_SSL, 277))
_error_codes.append(("SHORT_READ", lib.ERR_LIB_SSL, 219))
_error_codes.append(("SIGNATURE_ALGORITHMS_ERROR", lib.ERR_LIB_SSL, 360))
_error_codes.append(("SIGNATURE_FOR_NON_SIGNING_CERTIFICATE", lib.ERR_LIB_SSL, 220))
_error_codes.append(("SRP_A_CALC", lib.ERR_LIB_SSL, 361))
_error_codes.append(("SRTP_COULD_NOT_ALLOCATE_PROFILES", lib.ERR_LIB_SSL, 362))
_error_codes.append(("SRTP_PROTECTION_PROFILE_LIST_TOO_LONG", lib.ERR_LIB_SSL, 363))
_error_codes.append(("SRTP_UNKNOWN_PROTECTION_PROFILE", lib.ERR_LIB_SSL, 364))
_error_codes.append(("SSL23_DOING_SESSION_ID_REUSE", lib.ERR_LIB_SSL, 221))
_error_codes.append(("SSL2_CONNECTION_ID_TOO_LONG", lib.ERR_LIB_SSL, 299))
_error_codes.append(("SSL3_EXT_INVALID_ECPOINTFORMAT", lib.ERR_LIB_SSL, 321))
_error_codes.append(("SSL3_EXT_INVALID_SERVERNAME", lib.ERR_LIB_SSL, 319))
_error_codes.append(("SSL3_EXT_INVALID_SERVERNAME_TYPE", lib.ERR_LIB_SSL, 320))
_error_codes.append(("SSL3_SESSION_ID_TOO_LONG", lib.ERR_LIB_SSL, 300))
_error_codes.append(("SSL3_SESSION_ID_TOO_SHORT", lib.ERR_LIB_SSL, 222))
_error_codes.append(("SSLV3_ALERT_BAD_CERTIFICATE", lib.ERR_LIB_SSL, 1042))
_error_codes.append(("SSLV3_ALERT_BAD_RECORD_MAC", lib.ERR_LIB_SSL, 1020))
_error_codes.append(("SSLV3_ALERT_CERTIFICATE_EXPIRED", lib.ERR_LIB_SSL, 1045))
_error_codes.append(("SSLV3_ALERT_CERTIFICATE_REVOKED", lib.ERR_LIB_SSL, 1044))
_error_codes.append(("SSLV3_ALERT_CERTIFICATE_UNKNOWN", lib.ERR_LIB_SSL, 1046))
_error_codes.append(("SSLV3_ALERT_DECOMPRESSION_FAILURE", lib.ERR_LIB_SSL, 1030))
_error_codes.append(("SSLV3_ALERT_HANDSHAKE_FAILURE", lib.ERR_LIB_SSL, 1040))
_error_codes.append(("SSLV3_ALERT_ILLEGAL_PARAMETER", lib.ERR_LIB_SSL, 1047))
_error_codes.append(("SSLV3_ALERT_NO_CERTIFICATE", lib.ERR_LIB_SSL, 1041))
_error_codes.append(("SSLV3_ALERT_UNEXPECTED_MESSAGE", lib.ERR_LIB_SSL, 1010))
_error_codes.append(("SSLV3_ALERT_UNSUPPORTED_CERTIFICATE", lib.ERR_LIB_SSL, 1043))
_error_codes.append(("SSL_CTX_HAS_NO_DEFAULT_SSL_VERSION", lib.ERR_LIB_SSL, 228))
_error_codes.append(("SSL_HANDSHAKE_FAILURE", lib.ERR_LIB_SSL, 229))
_error_codes.append(("SSL_LIBRARY_HAS_NO_CIPHERS", lib.ERR_LIB_SSL, 230))
_error_codes.append(("SSL_NEGATIVE_LENGTH", lib.ERR_LIB_SSL, 372))
_error_codes.append(("SSL_SESSION_ID_CALLBACK_FAILED", lib.ERR_LIB_SSL, 301))
_error_codes.append(("SSL_SESSION_ID_CONFLICT", lib.ERR_LIB_SSL, 302))
_error_codes.append(("SSL_SESSION_ID_CONTEXT_TOO_LONG", lib.ERR_LIB_SSL, 273))
_error_codes.append(("SSL_SESSION_ID_HAS_BAD_LENGTH", lib.ERR_LIB_SSL, 303))
_error_codes.append(("SSL_SESSION_ID_IS_DIFFERENT", lib.ERR_LIB_SSL, 231))
_error_codes.append(("TLSV1_ALERT_ACCESS_DENIED", lib.ERR_LIB_SSL, 1049))
_error_codes.append(("TLSV1_ALERT_DECODE_ERROR", lib.ERR_LIB_SSL, 1050))
_error_codes.append(("TLSV1_ALERT_DECRYPTION_FAILED", lib.ERR_LIB_SSL, 1021))
_error_codes.append(("TLSV1_ALERT_DECRYPT_ERROR", lib.ERR_LIB_SSL, 1051))
_error_codes.append(("TLSV1_ALERT_EXPORT_RESTRICTION", lib.ERR_LIB_SSL, 1060))
_error_codes.append(("TLSV1_ALERT_INAPPROPRIATE_FALLBACK", lib.ERR_LIB_SSL, 1086))
_error_codes.append(("TLSV1_ALERT_INSUFFICIENT_SECURITY", lib.ERR_LIB_SSL, 1071))
_error_codes.append(("TLSV1_ALERT_INTERNAL_ERROR", lib.ERR_LIB_SSL, 1080))
_error_codes.append(("TLSV1_ALERT_NO_RENEGOTIATION", lib.ERR_LIB_SSL, 1100))
_error_codes.append(("TLSV1_ALERT_PROTOCOL_VERSION", lib.ERR_LIB_SSL, 1070))
_error_codes.append(("TLSV1_ALERT_RECORD_OVERFLOW", lib.ERR_LIB_SSL, 1022))
_error_codes.append(("TLSV1_ALERT_UNKNOWN_CA", lib.ERR_LIB_SSL, 1048))
_error_codes.append(("TLSV1_ALERT_USER_CANCELLED", lib.ERR_LIB_SSL, 1090))
_error_codes.append(("TLSV1_BAD_CERTIFICATE_HASH_VALUE", lib.ERR_LIB_SSL, 1114))
_error_codes.append(("TLSV1_BAD_CERTIFICATE_STATUS_RESPONSE", lib.ERR_LIB_SSL, 1113))
_error_codes.append(("TLSV1_CERTIFICATE_UNOBTAINABLE", lib.ERR_LIB_SSL, 1111))
_error_codes.append(("TLSV1_UNRECOGNIZED_NAME", lib.ERR_LIB_SSL, 1112))
_error_codes.append(("TLSV1_UNSUPPORTED_EXTENSION", lib.ERR_LIB_SSL, 1110))
_error_codes.append(("TLS_CLIENT_CERT_REQ_WITH_ANON_CIPHER", lib.ERR_LIB_SSL, 232))
_error_codes.append(("TLS_HEARTBEAT_PEER_DOESNT_ACCEPT", lib.ERR_LIB_SSL, 365))
_error_codes.append(("TLS_HEARTBEAT_PENDING", lib.ERR_LIB_SSL, 366))
_error_codes.append(("TLS_ILLEGAL_EXPORTER_LABEL", lib.ERR_LIB_SSL, 367))
_error_codes.append(("TLS_INVALID_ECPOINTFORMAT_LIST", lib.ERR_LIB_SSL, 157))
_error_codes.append(("TLS_PEER_DID_NOT_RESPOND_WITH_CERTIFICATE_LIST", lib.ERR_LIB_SSL, 233))
_error_codes.append(("TLS_RSA_ENCRYPTED_VALUE_LENGTH_IS_WRONG", lib.ERR_LIB_SSL, 234))
_error_codes.append(("TRIED_TO_USE_UNSUPPORTED_CIPHER", lib.ERR_LIB_SSL, 235))
_error_codes.append(("UNABLE_TO_DECODE_DH_CERTS", lib.ERR_LIB_SSL, 236))
_error_codes.append(("UNABLE_TO_DECODE_ECDH_CERTS", lib.ERR_LIB_SSL, 313))
_error_codes.append(("UNABLE_TO_EXTRACT_PUBLIC_KEY", lib.ERR_LIB_SSL, 237))
_error_codes.append(("UNABLE_TO_FIND_DH_PARAMETERS", lib.ERR_LIB_SSL, 238))
_error_codes.append(("UNABLE_TO_FIND_ECDH_PARAMETERS", lib.ERR_LIB_SSL, 314))
_error_codes.append(("UNABLE_TO_FIND_PUBLIC_KEY_PARAMETERS", lib.ERR_LIB_SSL, 239))
_error_codes.append(("UNABLE_TO_FIND_SSL_METHOD", lib.ERR_LIB_SSL, 240))
_error_codes.append(("UNABLE_TO_LOAD_SSL2_MD5_ROUTINES", lib.ERR_LIB_SSL, 241))
_error_codes.append(("UNABLE_TO_LOAD_SSL3_MD5_ROUTINES", lib.ERR_LIB_SSL, 242))
_error_codes.append(("UNABLE_TO_LOAD_SSL3_SHA1_ROUTINES", lib.ERR_LIB_SSL, 243))
_error_codes.append(("UNEXPECTED_MESSAGE", lib.ERR_LIB_SSL, 244))
_error_codes.append(("UNEXPECTED_RECORD", lib.ERR_LIB_SSL, 245))
_error_codes.append(("UNINITIALIZED", lib.ERR_LIB_SSL, 276))
_error_codes.append(("UNKNOWN_ALERT_TYPE", lib.ERR_LIB_SSL, 246))
_error_codes.append(("UNKNOWN_CERTIFICATE_TYPE", lib.ERR_LIB_SSL, 247))
_error_codes.append(("UNKNOWN_CIPHER_RETURNED", lib.ERR_LIB_SSL, 248))
_error_codes.append(("UNKNOWN_CIPHER_TYPE", lib.ERR_LIB_SSL, 249))
_error_codes.append(("UNKNOWN_CMD_NAME", lib.ERR_LIB_SSL, 386))
_error_codes.append(("UNKNOWN_DIGEST", lib.ERR_LIB_SSL, 368))
_error_codes.append(("UNKNOWN_KEY_EXCHANGE_TYPE", lib.ERR_LIB_SSL, 250))
_error_codes.append(("UNKNOWN_PKEY_TYPE", lib.ERR_LIB_SSL, 251))
_error_codes.append(("UNKNOWN_PROTOCOL", lib.ERR_LIB_SSL, 252))
_error_codes.append(("UNKNOWN_REMOTE_ERROR_TYPE", lib.ERR_LIB_SSL, 253))
_error_codes.append(("UNKNOWN_SSL_VERSION", lib.ERR_LIB_SSL, 254))
_error_codes.append(("UNKNOWN_STATE", lib.ERR_LIB_SSL, 255))
_error_codes.append(("UNSAFE_LEGACY_RENEGOTIATION_DISABLED", lib.ERR_LIB_SSL, 338))
_error_codes.append(("UNSUPPORTED_CIPHER", lib.ERR_LIB_SSL, 256))
_error_codes.append(("UNSUPPORTED_COMPRESSION_ALGORITHM", lib.ERR_LIB_SSL, 257))
_error_codes.append(("UNSUPPORTED_DIGEST_TYPE", lib.ERR_LIB_SSL, 326))
_error_codes.append(("UNSUPPORTED_ELLIPTIC_CURVE", lib.ERR_LIB_SSL, 315))
_error_codes.append(("UNSUPPORTED_PROTOCOL", lib.ERR_LIB_SSL, 258))
_error_codes.append(("UNSUPPORTED_SSL_VERSION", lib.ERR_LIB_SSL, 259))
_error_codes.append(("UNSUPPORTED_STATUS_TYPE", lib.ERR_LIB_SSL, 329))
_error_codes.append(("USE_SRTP_NOT_NEGOTIATED", lib.ERR_LIB_SSL, 369))
_error_codes.append(("VERSION_TOO_LOW", lib.ERR_LIB_SSL, 396))
_error_codes.append(("WRITE_BIO_NOT_SET", lib.ERR_LIB_SSL, 260))
_error_codes.append(("WRONG_CERTIFICATE_TYPE", lib.ERR_LIB_SSL, 383))
_error_codes.append(("WRONG_CIPHER_RETURNED", lib.ERR_LIB_SSL, 261))
_error_codes.append(("WRONG_CURVE", lib.ERR_LIB_SSL, 378))
_error_codes.append(("WRONG_MESSAGE_TYPE", lib.ERR_LIB_SSL, 262))
_error_codes.append(("WRONG_NUMBER_OF_KEY_BITS", lib.ERR_LIB_SSL, 263))
_error_codes.append(("WRONG_SIGNATURE_LENGTH", lib.ERR_LIB_SSL, 264))
_error_codes.append(("WRONG_SIGNATURE_SIZE", lib.ERR_LIB_SSL, 265))
_error_codes.append(("WRONG_SIGNATURE_TYPE", lib.ERR_LIB_SSL, 370))
_error_codes.append(("WRONG_SSL_VERSION", lib.ERR_LIB_SSL, 266))
_error_codes.append(("WRONG_VERSION_NUMBER", lib.ERR_LIB_SSL, 267))
_error_codes.append(("X509_LIB", lib.ERR_LIB_SSL, 268))
_error_codes.append(("X509_VERIFICATION_SETUP_PROBLEMS", lib.ERR_LIB_SSL, 269))
_error_codes.append(("AKID_MISMATCH", lib.ERR_LIB_X509, 110))
_error_codes.append(("BAD_X509_FILETYPE", lib.ERR_LIB_X509, 100))
_error_codes.append(("BASE64_DECODE_ERROR", lib.ERR_LIB_X509, 118))
_error_codes.append(("CANT_CHECK_DH_KEY", lib.ERR_LIB_X509, 114))
_error_codes.append(("CERT_ALREADY_IN_HASH_TABLE", lib.ERR_LIB_X509, 101))
_error_codes.append(("CRL_ALREADY_DELTA", lib.ERR_LIB_X509, 127))
_error_codes.append(("CRL_VERIFY_FAILURE", lib.ERR_LIB_X509, 131))
_error_codes.append(("ERR_ASN1_LIB", lib.ERR_LIB_X509, 102))
_error_codes.append(("IDP_MISMATCH", lib.ERR_LIB_X509, 128))
_error_codes.append(("INVALID_DIRECTORY", lib.ERR_LIB_X509, 113))
_error_codes.append(("INVALID_FIELD_NAME", lib.ERR_LIB_X509, 119))
_error_codes.append(("INVALID_TRUST", lib.ERR_LIB_X509, 123))
_error_codes.append(("ISSUER_MISMATCH", lib.ERR_LIB_X509, 129))
_error_codes.append(("KEY_TYPE_MISMATCH", lib.ERR_LIB_X509, 115))
_error_codes.append(("KEY_VALUES_MISMATCH", lib.ERR_LIB_X509, 116))
_error_codes.append(("LOADING_CERT_DIR", lib.ERR_LIB_X509, 103))
_error_codes.append(("LOADING_DEFAULTS", lib.ERR_LIB_X509, 104))
_error_codes.append(("METHOD_NOT_SUPPORTED", lib.ERR_LIB_X509, 124))
_error_codes.append(("NEWER_CRL_NOT_NEWER", lib.ERR_LIB_X509, 132))
_error_codes.append(("NO_CERT_SET_FOR_US_TO_VERIFY", lib.ERR_LIB_X509, 105))
_error_codes.append(("NO_CRL_NUMBER", lib.ERR_LIB_X509, 130))
_error_codes.append(("PUBLIC_KEY_DECODE_ERROR", lib.ERR_LIB_X509, 125))
_error_codes.append(("PUBLIC_KEY_ENCODE_ERROR", lib.ERR_LIB_X509, 126))
_error_codes.append(("SHOULD_RETRY", lib.ERR_LIB_X509, 106))
_error_codes.append(("UNABLE_TO_FIND_PARAMETERS_IN_CHAIN", lib.ERR_LIB_X509, 107))
_error_codes.append(("UNABLE_TO_GET_CERTS_PUBLIC_KEY", lib.ERR_LIB_X509, 108))
_error_codes.append(("UNKNOWN_KEY_TYPE", lib.ERR_LIB_X509, 117))
_error_codes.append(("UNKNOWN_NID", lib.ERR_LIB_X509, 109))
_error_codes.append(("UNKNOWN_PURPOSE_ID", lib.ERR_LIB_X509, 121))
_error_codes.append(("UNKNOWN_TRUST_ID", lib.ERR_LIB_X509, 120))
_error_codes.append(("UNSUPPORTED_ALGORITHM", lib.ERR_LIB_X509, 111))
_error_codes.append(("WRONG_LOOKUP_TYPE", lib.ERR_LIB_X509, 112))
_error_codes.append(("WRONG_TYPE", lib.ERR_LIB_X509, 122))

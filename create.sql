--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 16.0

-- Started on 2023-11-02 09:33:31 CET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 16656)
-- Name: comment_like; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.comment_like (
    eventid integer NOT NULL,
    userid integer NOT NULL,
    commentid integer NOT NULL
);


ALTER TABLE public.comment_like OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16643)
-- Name: event_like; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event_like (
    eventid integer NOT NULL,
    userid integer NOT NULL
);


ALTER TABLE public.event_like OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16585)
-- Name: events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.events (
    eventid integer NOT NULL,
    title character varying(150) NOT NULL,
    description text NOT NULL,
    address character varying(200) NOT NULL,
    image character varying(200),
    event_date date NOT NULL,
    likes integer DEFAULT 0 NOT NULL,
    price double precision
);


ALTER TABLE public.events OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16584)
-- Name: events_eventid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.events ALTER COLUMN eventid ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.events_eventid_seq
    START WITH 1000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 219 (class 1259 OID 16624)
-- Name: user_comments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_comments (
    commentid integer NOT NULL,
    eventid integer NOT NULL,
    userid integer NOT NULL,
    content text NOT NULL,
    "timestamp" date NOT NULL
);


ALTER TABLE public.user_comments OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16623)
-- Name: user_comments_commentid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.user_comments ALTER COLUMN commentid ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.user_comments_commentid_seq
    START WITH 1000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 16594)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    userid integer NOT NULL,
    email character varying(150) NOT NULL,
    user_password text NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16593)
-- Name: users_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users ALTER COLUMN userid ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.users_userid_seq
    START WITH 1000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3823 (class 2606 OID 16630)
-- Name: user_comments comment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_comments
    ADD CONSTRAINT comment_pkey PRIMARY KEY (commentid);


--
-- TOC entry 3817 (class 2606 OID 16592)
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (eventid);


--
-- TOC entry 3825 (class 2606 OID 16632)
-- Name: user_comments user_comments_content_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_comments
    ADD CONSTRAINT user_comments_content_key UNIQUE (content);


--
-- TOC entry 3819 (class 2606 OID 16600)
-- Name: users user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT user_pkey PRIMARY KEY (userid);


--
-- TOC entry 3821 (class 2606 OID 16602)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 3830 (class 2606 OID 16669)
-- Name: comment_like fk_comment; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comment_like
    ADD CONSTRAINT fk_comment FOREIGN KEY (commentid) REFERENCES public.user_comments(commentid);


--
-- TOC entry 3826 (class 2606 OID 16633)
-- Name: user_comments fk_event; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_comments
    ADD CONSTRAINT fk_event FOREIGN KEY (eventid) REFERENCES public.events(eventid);


--
-- TOC entry 3828 (class 2606 OID 16646)
-- Name: event_like fk_event; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_like
    ADD CONSTRAINT fk_event FOREIGN KEY (eventid) REFERENCES public.events(eventid);


--
-- TOC entry 3831 (class 2606 OID 16659)
-- Name: comment_like fk_event; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comment_like
    ADD CONSTRAINT fk_event FOREIGN KEY (eventid) REFERENCES public.events(eventid);


--
-- TOC entry 3827 (class 2606 OID 16638)
-- Name: user_comments fk_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_comments
    ADD CONSTRAINT fk_user FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- TOC entry 3829 (class 2606 OID 16651)
-- Name: event_like fk_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_like
    ADD CONSTRAINT fk_user FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- TOC entry 3832 (class 2606 OID 16664)
-- Name: comment_like fk_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.comment_like
    ADD CONSTRAINT fk_user FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- TOC entry 3980 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: pg_database_owner
--

GRANT ALL ON SCHEMA public TO cloudsqlsuperuser;


--
-- TOC entry 3981 (class 0 OID 0)
-- Dependencies: 228
-- Name: FUNCTION pg_replication_origin_advance(text, pg_lsn); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_advance(text, pg_lsn) TO cloudsqlsuperuser;


--
-- TOC entry 3982 (class 0 OID 0)
-- Dependencies: 232
-- Name: FUNCTION pg_replication_origin_create(text); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_create(text) TO cloudsqlsuperuser;


--
-- TOC entry 3983 (class 0 OID 0)
-- Dependencies: 223
-- Name: FUNCTION pg_replication_origin_drop(text); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_drop(text) TO cloudsqlsuperuser;


--
-- TOC entry 3984 (class 0 OID 0)
-- Dependencies: 233
-- Name: FUNCTION pg_replication_origin_oid(text); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_oid(text) TO cloudsqlsuperuser;


--
-- TOC entry 3985 (class 0 OID 0)
-- Dependencies: 229
-- Name: FUNCTION pg_replication_origin_progress(text, boolean); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_progress(text, boolean) TO cloudsqlsuperuser;


--
-- TOC entry 3986 (class 0 OID 0)
-- Dependencies: 224
-- Name: FUNCTION pg_replication_origin_session_is_setup(); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_session_is_setup() TO cloudsqlsuperuser;


--
-- TOC entry 3987 (class 0 OID 0)
-- Dependencies: 225
-- Name: FUNCTION pg_replication_origin_session_progress(boolean); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_session_progress(boolean) TO cloudsqlsuperuser;


--
-- TOC entry 3988 (class 0 OID 0)
-- Dependencies: 226
-- Name: FUNCTION pg_replication_origin_session_reset(); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_session_reset() TO cloudsqlsuperuser;


--
-- TOC entry 3989 (class 0 OID 0)
-- Dependencies: 227
-- Name: FUNCTION pg_replication_origin_session_setup(text); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_session_setup(text) TO cloudsqlsuperuser;


--
-- TOC entry 3990 (class 0 OID 0)
-- Dependencies: 230
-- Name: FUNCTION pg_replication_origin_xact_reset(); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_xact_reset() TO cloudsqlsuperuser;


--
-- TOC entry 3991 (class 0 OID 0)
-- Dependencies: 222
-- Name: FUNCTION pg_replication_origin_xact_setup(pg_lsn, timestamp with time zone); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_replication_origin_xact_setup(pg_lsn, timestamp with time zone) TO cloudsqlsuperuser;


--
-- TOC entry 3992 (class 0 OID 0)
-- Dependencies: 231
-- Name: FUNCTION pg_show_replication_origin_status(OUT local_id oid, OUT external_id text, OUT remote_lsn pg_lsn, OUT local_lsn pg_lsn); Type: ACL; Schema: pg_catalog; Owner: cloudsqladmin
--

GRANT ALL ON FUNCTION pg_catalog.pg_show_replication_origin_status(OUT local_id oid, OUT external_id text, OUT remote_lsn pg_lsn, OUT local_lsn pg_lsn) TO cloudsqlsuperuser;


-- Completed on 2023-11-02 09:33:36 CET

--
-- PostgreSQL database dump complete
--


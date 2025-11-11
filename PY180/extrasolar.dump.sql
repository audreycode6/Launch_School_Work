--
-- PostgreSQL database dump
--

\restrict 6d7EO9s9qVlQ4axyp5NlUcNgFrMh0h1aOJ1GLFNIKE0PzBeAqNQ5MEPVvnW3NuO

-- Dumped from database version 14.19 (Homebrew)
-- Dumped by pg_dump version 14.19 (Homebrew)

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

--
-- Name: valid_spectral_type; Type: TYPE; Schema: public; Owner: audrey
--

CREATE TYPE public.valid_spectral_type AS ENUM (
    'O',
    'B',
    'A',
    'F',
    'G',
    'K',
    'M'
);


ALTER TYPE public.valid_spectral_type OWNER TO audrey;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: moons; Type: TABLE; Schema: public; Owner: audrey
--

CREATE TABLE public.moons (
    id integer NOT NULL,
    designation integer NOT NULL,
    semi_major_axis numeric,
    mass numeric,
    planet_id integer NOT NULL,
    CONSTRAINT moons_designation_check CHECK ((designation > 0)),
    CONSTRAINT moons_mass_check CHECK ((mass > (0)::numeric)),
    CONSTRAINT moons_semi_major_axis_check CHECK ((semi_major_axis > (0)::numeric))
);


ALTER TABLE public.moons OWNER TO audrey;

--
-- Name: moons_id_seq; Type: SEQUENCE; Schema: public; Owner: audrey
--

CREATE SEQUENCE public.moons_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moons_id_seq OWNER TO audrey;

--
-- Name: moons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: audrey
--

ALTER SEQUENCE public.moons_id_seq OWNED BY public.moons.id;


--
-- Name: planets; Type: TABLE; Schema: public; Owner: audrey
--

CREATE TABLE public.planets (
    id integer NOT NULL,
    designation character varying(1) NOT NULL,
    mass numeric NOT NULL,
    stars_id integer NOT NULL,
    semi_major_axis numeric NOT NULL,
    CONSTRAINT planets_designation_check CHECK ((length((designation)::text) = 1)),
    CONSTRAINT planets_mass_check CHECK ((mass > (0)::numeric))
);


ALTER TABLE public.planets OWNER TO audrey;

--
-- Name: planets_id_seq; Type: SEQUENCE; Schema: public; Owner: audrey
--

CREATE SEQUENCE public.planets_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planets_id_seq OWNER TO audrey;

--
-- Name: planets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: audrey
--

ALTER SEQUENCE public.planets_id_seq OWNED BY public.planets.id;


--
-- Name: stars; Type: TABLE; Schema: public; Owner: audrey
--

CREATE TABLE public.stars (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    distance numeric NOT NULL,
    spectral_type public.valid_spectral_type NOT NULL,
    companions integer NOT NULL,
    CONSTRAINT stars_companions_check CHECK ((companions >= 0)),
    CONSTRAINT stars_distance_check CHECK ((distance > (0)::numeric)),
    CONSTRAINT stars_spectral_type_check CHECK ((length((spectral_type)::text) = 1))
);


ALTER TABLE public.stars OWNER TO audrey;

--
-- Name: stars_id_seq; Type: SEQUENCE; Schema: public; Owner: audrey
--

CREATE SEQUENCE public.stars_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stars_id_seq OWNER TO audrey;

--
-- Name: stars_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: audrey
--

ALTER SEQUENCE public.stars_id_seq OWNED BY public.stars.id;


--
-- Name: moons id; Type: DEFAULT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.moons ALTER COLUMN id SET DEFAULT nextval('public.moons_id_seq'::regclass);


--
-- Name: planets id; Type: DEFAULT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.planets ALTER COLUMN id SET DEFAULT nextval('public.planets_id_seq'::regclass);


--
-- Name: stars id; Type: DEFAULT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.stars ALTER COLUMN id SET DEFAULT nextval('public.stars_id_seq'::regclass);


--
-- Data for Name: moons; Type: TABLE DATA; Schema: public; Owner: audrey
--



--
-- Data for Name: planets; Type: TABLE DATA; Schema: public; Owner: audrey
--

INSERT INTO public.planets VALUES (1, 'b', 0.0036, 3, 23.5);
INSERT INTO public.planets VALUES (2, 'c', 0.1, 4, 3.465);


--
-- Data for Name: stars; Type: TABLE DATA; Schema: public; Owner: audrey
--

INSERT INTO public.stars VALUES (3, 'Alpha Centauri B', 4.37, 'K', 3);
INSERT INTO public.stars VALUES (4, 'Epsilon Eridani', 10.5, 'K', 0);


--
-- Name: moons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: audrey
--

SELECT pg_catalog.setval('public.moons_id_seq', 1, false);


--
-- Name: planets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: audrey
--

SELECT pg_catalog.setval('public.planets_id_seq', 2, true);


--
-- Name: stars_id_seq; Type: SEQUENCE SET; Schema: public; Owner: audrey
--

SELECT pg_catalog.setval('public.stars_id_seq', 4, true);


--
-- Name: moons moons_pkey; Type: CONSTRAINT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.moons
    ADD CONSTRAINT moons_pkey PRIMARY KEY (id);


--
-- Name: planets planets_pkey; Type: CONSTRAINT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.planets
    ADD CONSTRAINT planets_pkey PRIMARY KEY (id);


--
-- Name: stars stars_name_key; Type: CONSTRAINT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.stars
    ADD CONSTRAINT stars_name_key UNIQUE (name);


--
-- Name: stars stars_pkey; Type: CONSTRAINT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.stars
    ADD CONSTRAINT stars_pkey PRIMARY KEY (id);


--
-- Name: moons moons_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.moons
    ADD CONSTRAINT moons_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planets(id);


--
-- Name: planets planets_stars_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: audrey
--

ALTER TABLE ONLY public.planets
    ADD CONSTRAINT planets_stars_id_fkey FOREIGN KEY (stars_id) REFERENCES public.stars(id);


--
-- PostgreSQL database dump complete
--

\unrestrict 6d7EO9s9qVlQ4axyp5NlUcNgFrMh0h1aOJ1GLFNIKE0PzBeAqNQ5MEPVvnW3NuO


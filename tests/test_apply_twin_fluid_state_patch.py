from tools.apply_twin_fluid_state_patch import patch_state_source


def fixture():
    return r'''
        pfD, pfS, pftau,                  //!< State variables for the PF
        p,                         //!< Separation between two metrics (relative shift)
        Lt,                        //!< Lorentz factor (derived from `p`)
        R,                         //!< Ratio `fB/gB`
        pfv,                       //!< The three-velocity of the PF
        mpiBoundary = pfv,
        pfD_t, pfS_t, pftau_t, p_t,
        pfD_r, pfS_r, pftau_r, pfv_r,

        p,
        pfD, pfS, pftau
    };

        { pfD, pfD_t },  { pfS, pfS_t },  { pftau, pftau_t }
    };

        { pfD,      "pfD",      "D" },
        { pfS,      "pfS",      "S" },
        { pftau,    "pftau",    "tau" },
        { pfv,      "pfv",      "v" },
        { pfD_t,    "pfD_t",    "Dt" },
        { pfS_t,    "pfS_t",    "St" },
        { pftau_t,  "pftau_t",  "\\partial_t \\hat\\tau"          },

        { pfD_r,    "pfD_r",    "Dr" },
        { pfS_r,    "pfS_r",    "Sr" },
        { pftau_r,  "pftau_r",  "taur" },
        { pfv_r,    "pfv_r",    "\\partial_r \\hat v"             },

    emitField(pfD)     emitField(pfD_t)
    emitField(pfS)     emitField(pfS_t)
    emitField(pftau)   emitField(pftau_t)
    emitField(pfv)     emitField(pfv_r)

    emitDerivative_r( pfD   )
    emitDerivative_r( pfS   )
    emitDerivative_r( pftau )

    Real eq_pf_D_t    ( Int m, Int n );
    Real eq_pf_S_t    ( Int m, Int n );
    Real eq_pf_tau_t  ( Int m, Int n );
    Real eq_pf_rho    ( Int m, Int n );
    Real eq_pf_j      ( Int m, Int n );
    Real eq_pf_J1     ( Int m, Int n );
    Real eq_pf_J2     ( Int m, Int n );

        pfv(m,n) = pfS(m,n) == 0 ? 0 : eq_pf_v(m,n);

        pfD   (m,n) = pfD    (m,nR);
        pfS   (m,n) = -pfS   (m,nR);
        pftau (m,n) = pftau  (m,nR);
        pfv   (m,n) = -pfv   (m,nR);

        extrapolate_R( fld::pfD,   m, n );
        extrapolate_R( fld::pfS,   m, n );
        extrapolate_R( fld::pftau, m, n );
        extrapolate_R( fld::pfv, m, n );

        pfD_r  (m,n) = GF_r( pfD,   m,n );
        pfS_r  (m,n) = GF_r( pfS,   m,n );
        pftau_r(m,n) = GF_r( pftau, m,n );
        pfv_r(m,n) = pfS(m,n) == 0 ? 0 : eq_pf_v_r( m, n );

        pfD_t   (m,n) = eq_pf_D_t  (m,n);
        pfS_t   (m,n) = eq_pf_S_t  (m,n);
        pftau_t (m,n) = eq_pf_tau_t(m,n);
'''


def test_state_patch_registers_and_evolves_independent_f_fluid():
    out = patch_state_source(fixture())
    for token in [
        "pfFD", "pfFS", "pfFtau", "pfFv",
        "pfFD_t", "pfFS_t", "pfFtau_t",
        "pfFD_r", "pfFS_r", "pfFtau_r", "pfFv_r",
    ]:
        assert token in out
    assert "mpiBoundary = pfFv" in out
    assert "{ pfFD, pfFD_t }" in out
    assert "pfFv(m,n) = pfFS(m,n) == 0 ? 0 : eq_pf_Fv(m,n);" in out
    assert "pfFD   (m,n) = pfFD    (m,nR);" in out
    assert "pfFS   (m,n) = -pfFS   (m,nR);" in out
    assert "extrapolate_R( fld::pfFD" in out
    assert "pfFD_t   (m,n) = eq_pf_FD_t" in out


def test_state_patch_preserves_g_fluid_lines():
    src = fixture()
    out = patch_state_source(src)
    assert "pfD_t   (m,n) = eq_pf_D_t  (m,n);" in out
    assert "pfv(m,n) = pfS(m,n) == 0 ? 0 : eq_pf_v(m,n);" in out

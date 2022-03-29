import React from 'react';
import { Trans } from '@lingui/macro';
import { Route, Switch, useRouteMatch } from 'react-router-dom';
import { Flex, Link } from '@ecostake/core';
import LayoutMain from '../layout/LayoutMain';

import { StakeHeaderTarget } from './StakeHeader';
import StakeMain from './StakeMain';


export default function Stake() {
  const { path } = useRouteMatch();

  return (
    <LayoutMain
      title={
        <>
          <Link to="/dashboard/stake" color="textPrimary">
            <Trans>Stake</Trans>
          </Link>
          <StakeHeaderTarget />
        </>
      }
    >

    <StakeMain />

    </LayoutMain>
  );
}

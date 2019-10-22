import React from "react";
import {VegaLite} from 'react-vega';

const Chart = ({spec}) => {
  if ('$schema' in spec) {
    return (
      <Grid.Row>
        <Grid.Column>
          <VegaLite spec={spec} />
        </Grid.Column>
      </Grid.Row>
    );
  } else {
    return 'Error: Incorrect chart specification';
  }
};

export default Chart;

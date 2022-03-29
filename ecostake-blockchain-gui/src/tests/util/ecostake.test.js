const ecostake = require('../../util/ecostake');

describe('ecostake', () => {
  it('converts number mojo to ecostake', () => {
    const result = ecostake.mojo_to_ecostake(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to ecostake', () => {
    const result = ecostake.mojo_to_ecostake('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to ecostake string', () => {
    const result = ecostake.mojo_to_ecostake_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to ecostake string', () => {
    const result = ecostake.mojo_to_ecostake_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number ecostake to mojo', () => {
    const result = ecostake.ecostake_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string ecostake to mojo', () => {
    const result = ecostake.ecostake_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = ecostake.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = ecostake.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = ecostake.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = ecostake.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = ecostake.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = ecostake.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
